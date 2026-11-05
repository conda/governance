import base64
import copy
import io
import json
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import Mock, patch

from ruamel.yaml import YAML

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import sync_team_request
from sync_team_request import GitHub, render_team, sync_issue

ISSUE_URL = "https://github.com/conda/governance/issues/999"


def request_body(**changes):
    fields = {
        "Type of Team": "Sub-team (Dynamic Charter)",
        "Team Name": "example-team",
        "Team Handle": "@conda/example-team",
        "Members": "@zoe\n@alice",
        "Charter": "Maintain the example tools.\n\nMembership follows the governance policy.",
        "Responsibilities": "Review changes and publish releases.",
        "Scope": "The example tools and their documentation.",
        "Checklist": "- [x] I understand that an approved request needs a merged record PR.",
    }
    fields.update(changes)
    return "\n\n".join(
        f"### {heading}\n\n{value}"
        for heading, value in fields.items()
        if value is not None
    )


class RenderTeamTests(unittest.TestCase):
    def render(self, body):
        result = render_team(body, ISSUE_URL)
        self.assertIsNotNone(result)
        path, contents = result
        self.assertIsInstance(contents, str)
        data = YAML(typ="safe").load(contents)
        return path, contents, data

    def test_draft_records_requested_team_without_inventing_approval(self):
        path, _, data = self.render(request_body())

        self.assertEqual(path, "teams/example-team.yml")
        self.assertEqual(data["name"], "example-team")
        self.assertEqual(data["charter"], "dynamic-subteam")
        self.assertEqual(data["resources"]["teams"], ["conda/example-team"])
        self.assertFalse(data["resources"]["repos"])
        self.assertEqual(data["members"], {"alice": None, "zoe": None})
        self.assertEqual(data["links"], [ISSUE_URL])

    def test_team_type_mapping_does_not_guess_project_category(self):
        cases = {
            "Sub-team (Dynamic Charter)": "dynamic-subteam",
            "Sub-team (Static Charter)": "static-subteam",
            "Project Team": "unknown",
        }
        for selected, expected in cases.items():
            with self.subTest(selected=selected):
                _, _, data = self.render(
                    request_body(
                        **{
                            "Type of Team": selected,
                            "Team Handle": "conda-incubator/example-team",
                        }
                    )
                )
                self.assertEqual(data["charter"], expected)
                self.assertEqual(
                    data["resources"]["teams"], ["conda-incubator/example-team"]
                )

    def test_charter_sections_retain_text_and_nested_markdown(self):
        charter = (
            "Maintain tools without changing their licenses.\n\n"
            "### Operational notes\n"
            "Keep **these words** and the [policy](https://example.org/policy)."
        )
        responsibilities = "- Review contributions.\n- Preserve notices."
        scope = "Includes tools A and B.\nExcludes service C."
        _, _, data = self.render(
            request_body(
                Charter=charter, Responsibilities=responsibilities, Scope=scope
            )
        )

        details = data["details"]
        for heading, text in (
            ("## Role", charter),
            ("## Responsibility", responsibilities),
            ("## Scope", scope),
        ):
            with self.subTest(heading=heading):
                self.assertIn(heading, details)
                self.assertIn(text, details)

    def test_yaml_looking_charter_remains_text(self):
        charter = (
            "---\nname: another-team\nmembers:\n  attacker: approved\n"
            "payload: !!python/object/apply:os.system ['echo unsafe']\n"
            "alias: &approval true\ncopy: *approval"
        )
        _, _, data = self.render(request_body(Charter=charter))

        self.assertEqual(data["name"], "example-team")
        self.assertEqual(data["members"], {"alice": None, "zoe": None})
        self.assertIn(charter, data["details"])
        self.assertNotIn("payload", data)

    def test_missing_required_fields_in_known_request_are_rejected(self):
        for heading in ("Type of Team", "Team Name", "Team Handle", "Members"):
            for value in (None, "", "_No response_"):
                with (
                    self.subTest(heading=heading, value=value),
                    self.assertRaises(ValueError),
                ):
                    render_team(request_body(**{heading: value}), ISSUE_URL)

    def test_invalid_slug_cannot_choose_a_different_output_path(self):
        for name in (
            "../outside",
            "nested/team",
            "..\\outside",
            "/tmp/team",
            "Capitalized",
            "-leading-hyphen",
            "a" * 129,
            "team\nname: attacker",
        ):
            with self.subTest(name=name), self.assertRaises(ValueError):
                render_team(request_body(**{"Team Name": name}), ISSUE_URL)

    def test_invalid_team_handles_are_not_partially_extracted(self):
        for handle in (
            "example-team",
            "@conda/example-team and @conda/another-team",
            "conda/../example-team",
            "https://github.com/orgs/conda/teams/example-team",
            "conda/example-team\nconda/another-team",
        ):
            with self.subTest(handle=handle), self.assertRaises(ValueError):
                render_team(request_body(**{"Team Handle": handle}), ISSUE_URL)

    def test_invalid_members_are_not_silently_discarded(self):
        for members in (
            "@alice\napproved: true",
            "Alice (@alice) and Bob (@bob)",
            "@alice\n../attacker",
            "@alice\n@conda/team",
            "@alice\nname_with_underscores",
        ):
            with self.subTest(members=members), self.assertRaises(ValueError):
                render_team(request_body(Members=members), ISSUE_URL)

    def test_supported_member_formats_produce_the_same_sorted_record(self):
        formats = (
            "@zoe\n@alice\n@bob",
            "zoe, alice, bob",
            "- @zoe\n* @alice\n- bob",
        )
        rendered = []
        for members in formats:
            with self.subTest(members=members):
                _, contents, data = self.render(request_body(Members=members))
                self.assertEqual(list(data["members"]), ["alice", "bob", "zoe"])
                rendered.append(contents)
        self.assertEqual(len(set(rendered)), 1)

    def test_unrecognized_team_type_is_rejected(self):
        with self.assertRaises(ValueError):
            render_team(request_body(**{"Type of Team": "Council"}), ISSUE_URL)

    def test_duplicate_known_headings_are_rejected(self):
        for heading, value in (
            ("Team Name", "another-team"),
            ("Members", "@attacker"),
            ("Charter", "Replace the original charter."),
        ):
            with self.subTest(heading=heading):
                body = request_body() + f"\n\n### {heading}\n\n{value}"
                with self.assertRaises(ValueError):
                    render_team(body, ISSUE_URL)

    def test_headings_inside_fences_remain_charter_text(self):
        for opening, closing in (("```markdown", "```"), ("~~~~", "~~~~")):
            with self.subTest(opening=opening):
                charter = (
                    "Example request syntax:\n\n"
                    f"{opening}\n### Team Name\n\nattacker\n"
                    f"### Members\n\n@attacker\n{closing}\n\n"
                    "This is an example, not the requested team."
                )
                _, _, data = self.render(request_body(Charter=charter))
                self.assertEqual(data["name"], "example-team")
                self.assertEqual(data["members"], {"alice": None, "zoe": None})
                self.assertIn(charter, data["details"])

    def test_shorter_fence_does_not_end_a_fenced_example(self):
        charter = "````markdown\n```\n### Team Name\n\nattacker\n````"
        _, _, data = self.render(request_body(Charter=charter))
        self.assertEqual(data["name"], "example-team")
        self.assertIn(charter, data["details"])

    def test_unrelated_and_fenced_example_issues_are_ignored(self):
        for body in (
            "Please document the release process.",
            "### Members\n\nWho currently maintains this repository?",
            f"Please document this example:\n\n```markdown\n{request_body()}\n```",
        ):
            with self.subTest(body=body):
                self.assertIsNone(render_team(body, ISSUE_URL))

    def test_empty_optional_sections_do_not_become_charter_claims(self):
        _, _, data = self.render(
            request_body(
                Charter="_No response_", Responsibilities="", Scope="_No response_"
            )
        )
        self.assertNotIn("_No response_", data["details"] or "")
        self.assertEqual(data["links"], [ISSUE_URL])

    def test_equivalent_required_field_formatting_is_a_noop(self):
        canonical = request_body()
        padded = request_body(
            **{
                "Team Name": "  example-team  ",
                "Team Handle": "conda/example-team",
                "Members": "alice, zoe",
            }
        )
        self.assertEqual(
            render_team(canonical, ISSUE_URL), render_team(padded, ISSUE_URL)
        )


class FakeGitHub:
    """An in-memory GitHub repository, with no external calls."""

    def __init__(self, body=None, files=None):
        self.issue = {"state": "open", "body": request_body() if body is None else body}
        self.refs = {"main": "base"}
        self.trees = {"tree-base": dict(files or {})}
        self.commits = {
            "base": {
                "sha": "base",
                "tree": {"sha": "tree-base"},
                "parents": [],
                "committer": {"login": "maintainer"},
                "commit": {"message": "Initial state"},
            }
        }
        self.prs = []
        self.calls = []
        self.writes = []
        self.fail_pr_once = False

    def files_at(self, ref):
        sha = self.refs.get(ref, ref)
        return self.trees[self.commits[sha]["tree"]["sha"]]

    def get(self, path, *, missing_ok=False, **params):
        self.calls.append(("GET", path, params))
        if path == "":
            return {"default_branch": "main"}
        if path == "issues/999":
            return copy.deepcopy(self.issue)
        if path == "pulls/1000":
            pr = copy.deepcopy(self.prs[0])
            pr["head"]["sha"] = self.refs[pr["head"]["ref"]]
            return pr
        if path.startswith("git/ref/heads/"):
            sha = self.refs.get(path.removeprefix("git/ref/heads/"))
            if sha is None and missing_ok:
                return None
            if sha is not None:
                return {"object": {"sha": sha}}
        if path.startswith("contents/"):
            contents = self.files_at(params["ref"]).get(path.removeprefix("contents/"))
            if contents is None and missing_ok:
                return None
            if contents is not None:
                return {
                    "type": "file",
                    "encoding": "base64",
                    "content": base64.b64encode(contents.encode()).decode(),
                }
        if path.startswith("git/commits/"):
            return copy.deepcopy(self.commits[path.removeprefix("git/commits/")])
        if path.startswith("compare/"):
            base, head = path.removeprefix("compare/").split("...")
            before, after = self.files_at(base), self.files_at(head)
            return {
                "files": [
                    {
                        "filename": filename,
                        "status": "added" if filename not in before else "modified",
                    }
                    for filename in sorted(before.keys() | after.keys())
                    if before.get(filename) != after.get(filename)
                ]
            }
        raise AssertionError(f"Unexpected GET: {path}")

    def list(self, endpoint, **params):
        self.calls.append(("LIST", endpoint, params))
        if endpoint == "pulls":
            return iter(copy.deepcopy(self.prs))
        if endpoint == "commits":
            commits = []
            sha = params["sha"]
            while sha:
                commit = self.commits[sha]
                commits.append(copy.deepcopy(commit))
                sha = commit["parents"][0]["sha"] if commit["parents"] else None
            return iter(commits)
        raise AssertionError(f"Unexpected LIST: {endpoint}")

    def post(self, path, **data):
        self.writes.append(("POST", path, copy.deepcopy(data)))
        if path == "git/trees":
            tree = dict(self.trees[data["base_tree"]])
            for entry in data["tree"]:
                tree[entry["path"]] = entry["content"]
            sha = f"tree-{len(self.trees)}"
            self.trees[sha] = tree
            return {"sha": sha}
        if path == "git/commits":
            sha = f"commit-{len(self.commits)}"
            self.commits[sha] = {
                "sha": sha,
                "tree": {"sha": data["tree"]},
                "parents": [{"sha": parent} for parent in data["parents"]],
                "committer": {"login": "github-actions[bot]"},
                "commit": {"message": data["message"]},
            }
            return {"sha": sha}
        if path == "git/refs":
            branch = data["ref"].removeprefix("refs/heads/")
            if branch in self.refs:
                raise ValueError("Reference already exists")
            self.refs[branch] = data["sha"]
            return {"object": {"sha": data["sha"]}}
        if path == "pulls":
            if self.fail_pr_once:
                self.fail_pr_once = False
                raise RuntimeError("Temporary PR creation failure")
            pr = {
                "number": 1000,
                "state": "open",
                "merged_at": None,
                "draft": data["draft"],
                "body": data["body"],
                "user": {"login": "github-actions[bot]"},
                "head": {
                    "ref": data["head"],
                    "repo": {"full_name": "conda/governance"},
                },
                "base": {"ref": data["base"]},
                "html_url": "https://github.com/conda/governance/pull/1000",
            }
            self.prs.append(pr)
            return copy.deepcopy(pr)
        raise AssertionError(f"Unexpected POST: {path}")

    def patch(self, path, **data):
        self.writes.append(("PATCH", path, copy.deepcopy(data)))
        if path.startswith("git/refs/heads/"):
            branch = path.removeprefix("git/refs/heads/")
            commit = self.commits[data["sha"]]
            if data["force"] or commit["parents"] != [{"sha": self.refs[branch]}]:
                raise ValueError("Refusing non-fast-forward update")
            self.refs[branch] = data["sha"]
            return {"object": {"sha": data["sha"]}}
        raise AssertionError(f"Unexpected PATCH: {path}")

    def human_commit(self, changes):
        branch = "fix/team-request-999"
        parent = self.refs[branch]
        tree = dict(self.files_at(parent))
        tree.update(changes)
        tree_sha = f"tree-{len(self.trees)}"
        self.trees[tree_sha] = tree
        sha = f"commit-{len(self.commits)}"
        self.commits[sha] = {
            "sha": sha,
            "tree": {"sha": tree_sha},
            "parents": [{"sha": parent}],
            "committer": {"login": "maintainer"},
            "commit": {"message": "Complete the team record"},
        }
        self.refs[branch] = sha


class SyncIssueTests(unittest.TestCase):
    branch = "fix/team-request-999"
    team_path = "teams/example-team.yml"

    def created_request(self):
        api = FakeGitHub(files={"README.md": "Existing governance documentation.\n"})
        sync_issue(api, 999)
        api.writes.clear()
        api.calls.clear()
        return api

    def test_creation_changes_only_one_team_record_on_a_same_repo_draft(self):
        api = FakeGitHub(files={"README.md": "Existing governance documentation.\n"})
        sync_issue(api, 999)

        self.assertEqual(api.refs["main"], "base")
        self.assertEqual(len(api.prs), 1)
        self.assertTrue(api.prs[0]["draft"])
        self.assertEqual(api.prs[0]["head"]["ref"], self.branch)
        self.assertEqual(api.prs[0]["head"]["repo"]["full_name"], "conda/governance")
        trees = [data for _, path, data in api.writes if path == "git/trees"]
        self.assertEqual(len(trees), 1)
        self.assertEqual(len(trees[0]["tree"]), 1)
        change = trees[0]["tree"][0]
        self.assertEqual(
            {key: change[key] for key in ("path", "mode", "type")},
            {"path": self.team_path, "mode": "100644", "type": "blob"},
        )
        self.assertEqual(
            api.files_at(self.branch)["README.md"],
            "Existing governance documentation.\n",
        )
        record = YAML(typ="safe").load(change["content"])
        self.assertEqual(record["members"], {"alice": None, "zoe": None})
        self.assertEqual(record["links"], [ISSUE_URL])

    def test_duplicate_delivery_is_a_noop(self):
        api = self.created_request()
        head = api.refs[self.branch]

        sync_issue(api, 999)

        self.assertEqual(api.writes, [])
        self.assertEqual(api.refs[self.branch], head)

    def test_review_handoff_during_sync_does_not_publish_an_update(self):
        for changed in (
            {"draft": False},
            {"state": "closed"},
            {"merged_at": "2026-11-05T12:00:00Z"},
        ):
            with self.subTest(changed=changed):
                api = self.created_request()
                head = api.refs[self.branch]
                api.issue["body"] = request_body(Scope="Updated proposal.")
                get = api.get

                def refreshed_pr(endpoint, get=get, changed=changed, **params):
                    result = get(endpoint, **params)
                    if endpoint == "pulls/1000":
                        result.update(changed)
                    return result

                with patch.object(api, "get", side_effect=refreshed_pr):
                    sync_issue(api, 999)

                self.assertEqual(api.refs[self.branch], head)
                self.assertFalse(any(method == "PATCH" for method, _, _ in api.writes))

    def test_concurrent_head_change_does_not_publish_an_update(self):
        api = self.created_request()
        head = api.refs[self.branch]
        api.issue["body"] = request_body(Scope="Updated proposal.")
        get = api.get

        def refreshed_pr(endpoint, **params):
            result = get(endpoint, **params)
            if endpoint == "pulls/1000":
                result["head"]["sha"] = "new-maintainer-head"
            return result

        with (
            patch.object(api, "get", side_effect=refreshed_pr),
            self.assertRaisesRegex(ValueError, "changed during this run"),
        ):
            sync_issue(api, 999)

        self.assertEqual(api.refs[self.branch], head)
        self.assertFalse(any(method == "PATCH" for method, _, _ in api.writes))
        self.assertEqual(len(api.prs), 1)

    def test_issue_edit_updates_the_same_draft_without_force_pushing(self):
        api = self.created_request()
        head = api.refs[self.branch]
        api.issue["body"] = request_body(
            Scope="The approved scope is still under discussion."
        )

        sync_issue(api, 999)

        self.assertNotEqual(api.refs[self.branch], head)
        self.assertEqual(len(api.prs), 1)
        self.assertFalse(any(path == "pulls" for _, path, _ in api.writes))
        ref_updates = [data for method, _, data in api.writes if method == "PATCH"]
        self.assertEqual(len(ref_updates), 1)
        self.assertIs(ref_updates[0]["force"], False)
        self.assertEqual(api.refs["main"], "base")
        record = YAML(typ="safe").load(api.files_at(self.branch)[self.team_path])
        self.assertIn(
            "The approved scope is still under discussion.", record["details"]
        )

    def test_human_team_edits_are_preserved_and_stop_updates(self):
        api = self.created_request()
        manual = (
            api.files_at(self.branch)[self.team_path]
            + "# A maintainer reviewed this.\n"
        )
        api.human_commit({self.team_path: manual})
        api.issue["body"] = request_body(Scope="Changed issue scope.")

        with self.assertRaisesRegex(ValueError, "human edits"):
            sync_issue(api, 999)

        self.assertEqual(api.writes, [])
        self.assertEqual(api.files_at(self.branch)[self.team_path], manual)

    def test_unrelated_files_on_the_request_branch_are_not_overwritten(self):
        api = self.created_request()
        api.human_commit({"README.md": "A separate human change.\n"})
        api.issue["body"] = request_body(Scope="Changed issue scope.")

        with self.assertRaises(ValueError):
            sync_issue(api, 999)

        self.assertEqual(api.writes, [])
        self.assertEqual(
            api.files_at(self.branch)["README.md"], "A separate human change.\n"
        )

    def test_an_unowned_same_named_branch_is_not_adopted(self):
        api = self.created_request()
        api.prs.clear()
        for commit in api.commits.values():
            commit["committer"] = {"login": "maintainer"}

        with self.assertRaisesRegex(ValueError, "not created by this workflow"):
            sync_issue(api, 999)

        self.assertEqual(api.writes, [])
        self.assertEqual(api.prs, [])

    def test_existing_pull_request_must_belong_to_this_workflow(self):
        mutations = (
            lambda pr: pr.update(body="An unrelated PR with the same branch."),
            lambda pr: pr["user"].update(login="maintainer"),
            lambda pr: pr["head"]["repo"].update(full_name="someone/governance"),
            lambda pr: pr["base"].update(ref="release"),
        )
        for index, mutate in enumerate(mutations):
            with self.subTest(mutation=index):
                api = self.created_request()
                mutate(api.prs[0])
                api.issue["body"] = request_body(Scope="Changed issue scope.")
                with self.assertRaises(ValueError):
                    sync_issue(api, 999)
                self.assertEqual(api.writes, [])

    def test_closed_issue_does_not_change_the_draft(self):
        api = self.created_request()
        api.issue["state"] = "closed"
        api.issue["body"] = request_body(Scope="Changed issue scope.")

        sync_issue(api, 999)

        self.assertEqual(api.writes, [])
        self.assertEqual(len(api.prs), 1)

    def test_closed_merged_and_ready_prs_end_automatic_updates(self):
        cases = (
            {"state": "closed"},
            {"state": "closed", "merged_at": "2026-11-05T12:00:00Z"},
            {"state": "open", "draft": False},
        )
        for changes in cases:
            with self.subTest(changes=changes):
                api = self.created_request()
                api.prs[0].update(changes)
                api.issue["body"] = request_body(
                    Scope="Changed after the PR lifecycle ended."
                )

                sync_issue(api, 999)

                self.assertEqual(api.writes, [])
                self.assertEqual(len(api.prs), 1)

    def test_pr_creation_failure_can_recover_without_another_commit(self):
        api = FakeGitHub()
        api.fail_pr_once = True
        with self.assertRaisesRegex(RuntimeError, "Temporary PR creation failure"):
            sync_issue(api, 999)
        head = api.refs[self.branch]
        self.assertEqual(api.prs, [])
        api.writes.clear()

        sync_issue(api, 999)

        self.assertEqual(api.refs[self.branch], head)
        self.assertEqual(len(api.prs), 1)
        self.assertEqual([path for _, path, _ in api.writes], ["pulls"])

    def test_existing_team_on_default_branch_is_not_replaced(self):
        api = FakeGitHub(files={self.team_path: "An existing team record.\n"})

        with self.assertRaisesRegex(ValueError, "already exists"):
            sync_issue(api, 999)

        self.assertEqual(api.writes, [])
        self.assertEqual(
            api.files_at("main")[self.team_path], "An existing team record.\n"
        )

    def test_multiple_prs_for_one_issue_stop_synchronization(self):
        api = self.created_request()
        api.prs.append(copy.deepcopy(api.prs[0]))

        with self.assertRaisesRegex(ValueError, "multiple PRs"):
            sync_issue(api, 999)

        self.assertEqual(api.writes, [])

    def test_renaming_a_team_does_not_add_a_second_record(self):
        api = self.created_request()
        api.issue["body"] = request_body(**{"Team Name": "renamed-team"})

        with self.assertRaises(ValueError):
            sync_issue(api, 999)

        self.assertEqual(api.writes, [])
        self.assertNotIn("teams/renamed-team.yml", api.files_at(self.branch))

    def test_invalid_issue_edit_preserves_existing_draft(self):
        api = self.created_request()
        original = api.files_at(self.branch)[self.team_path]
        api.issue["body"] = request_body(Members="@alice and anybody else")

        with self.assertRaises(ValueError):
            sync_issue(api, 999)

        self.assertEqual(api.writes, [])
        self.assertEqual(api.files_at(self.branch)[self.team_path], original)

    def test_missing_branch_for_existing_pr_is_not_recreated(self):
        api = self.created_request()
        del api.refs[self.branch]

        with self.assertRaisesRegex(ValueError, "branch is missing"):
            sync_issue(api, 999)

        self.assertEqual(api.writes, [])

    def test_unrelated_issues_and_pull_request_payloads_are_ignored(self):
        for issue in (
            {"state": "open", "body": "Please update the meeting agenda."},
            {"state": "open", "body": request_body(), "pull_request": {}},
        ):
            with self.subTest(issue=issue):
                api = FakeGitHub()
                api.issue = issue
                sync_issue(api, 999)
                self.assertEqual(api.writes, [])


class WorkflowEntryTests(unittest.TestCase):
    def test_event_body_is_ignored_in_favor_of_latest_api_body(self):
        api = FakeGitHub(body=request_body(**{"Team Name": "latest-team"}))
        event = {
            "action": "edited",
            "repository": {"full_name": "conda/governance"},
            "issue": {
                "number": 999,
                "body": request_body(**{"Team Name": "stale-team"}),
            },
            "changes": {"body": {"from": "Previous issue body"}},
        }
        environment = {
            "GITHUB_REPOSITORY": "conda/governance",
            "GITHUB_EVENT_PATH": "event.json",
            "GH_TOKEN": "test-token",
        }
        with (
            patch.dict("os.environ", environment, clear=True),
            patch.object(Path, "read_text", return_value=json.dumps(event)),
            patch.object(sync_team_request, "GitHub", return_value=api) as client,
            redirect_stdout(io.StringIO()),
        ):
            sync_team_request.main()

        client.assert_called_once_with("test-token")
        self.assertIn("teams/latest-team.yml", api.files_at("fix/team-request-999"))
        self.assertNotIn("teams/stale-team.yml", api.files_at("fix/team-request-999"))

    def test_repository_and_issue_number_are_checked_before_client_creation(self):
        for repository, number in (
            ("someone/governance", 999),
            ("conda/governance", "999/../../pulls"),
            ("conda/governance", True),
            ("conda/governance", 0),
        ):
            with self.subTest(repository=repository, number=number):
                event = {
                    "action": "opened",
                    "repository": {"full_name": repository},
                    "issue": {"number": number},
                }
                environment = {
                    "GITHUB_REPOSITORY": "conda/governance",
                    "GITHUB_EVENT_PATH": "event.json",
                    "GH_TOKEN": "test-token",
                }
                with (
                    patch.dict("os.environ", environment, clear=True),
                    patch.object(Path, "read_text", return_value=json.dumps(event)),
                    patch.object(sync_team_request, "GitHub") as client,
                    self.assertRaises(ValueError),
                ):
                    sync_team_request.main()
                client.assert_not_called()

    def test_non_body_edits_do_not_start_synchronization(self):
        event = {
            "action": "edited",
            "repository": {"full_name": "conda/governance"},
            "issue": {"number": 999},
            "changes": {"title": {"from": "Previous title"}},
        }
        with (
            patch.dict(
                "os.environ",
                {
                    "GITHUB_REPOSITORY": "conda/governance",
                    "GITHUB_EVENT_PATH": "event.json",
                },
                clear=True,
            ),
            patch.object(Path, "read_text", return_value=json.dumps(event)),
            patch.object(sync_team_request, "GitHub") as client,
        ):
            sync_team_request.main()
        client.assert_not_called()


class GitHubClientTests(unittest.TestCase):
    def test_repository_metadata_url_has_no_trailing_slash(self):
        session = Mock()
        session.headers = {}
        with patch.object(sync_team_request.requests, "Session", return_value=session):
            GitHub("test-token").get("")

        session.request.assert_called_once_with(
            "GET",
            "https://api.github.com/repos/conda/governance",
            timeout=30,
            params={},
        )

    def test_commit_history_path_is_passed_as_a_query_parameter(self):
        session = Mock()
        session.headers = {}
        session.request.return_value.json.return_value = [{"sha": "bot-commit"}]
        with patch.object(sync_team_request.requests, "Session", return_value=session):
            commits = list(
                GitHub("test-token").list(
                    "commits", sha="branch-head", path="teams/example-team.yml"
                )
            )

        self.assertEqual(commits, [{"sha": "bot-commit"}])
        session.request.assert_called_once_with(
            "GET",
            "https://api.github.com/repos/conda/governance/commits",
            timeout=30,
            params={
                "per_page": 100,
                "page": 1,
                "sha": "branch-head",
                "path": "teams/example-team.yml",
            },
        )

    def test_untrusted_record_text_is_json_data_and_token_stays_in_header(self):
        session = Mock()
        session.headers = {}
        response = session.request.return_value
        response.json.return_value = {"sha": "tree-result"}
        charter = "$(echo unsafe)\n`echo unsafe`\nhttps://attacker.example/collect"
        data = {"tree": [{"path": "teams/example-team.yml", "content": charter}]}
        with patch.object(sync_team_request.requests, "Session", return_value=session):
            api = GitHub("test-token")
            api.post("git/trees", **data)

        self.assertEqual(session.headers["Authorization"], "Bearer test-token")
        session.request.assert_called_once_with(
            "POST",
            "https://api.github.com/repos/conda/governance/git/trees",
            timeout=30,
            json=data,
        )
        self.assertNotIn("test-token", json.dumps(data))
        response.raise_for_status.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
