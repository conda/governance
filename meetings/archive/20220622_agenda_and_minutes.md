---
tags: [meeting-notes]
---
# 2022-06-22 Conda Community Meeting

* [Meeting link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/UTC/2022-06-22/17:00/b/Conda%20community%20meeting)

## Attendees

| Name                     | Initials | Affiliation   | GH Username        |
| -------------------------| -------- | ------------- | ------------------ |
| Jannis Leidel            | JL       | Anaconda      | jezdez             |
| Dave Clements            | DPC      | Anaconda      | tnabtaf            |
| Bianca Henderson         | BH       | Anaconda      | beeankha           |
| Filipe Fernandes         | FF       | conda-forge   | ocefpaf            |
| John Kirkham             | JK       | cf/NVIDIA     | jakirkham          |
| Daniel Holth             | DH       | Anaconda      | dholth             |
| Ken Odegard              | KO       | Anaconda      | kenodegard         |
| Marius van Niekerk       | MvN      | Voltron Data  | mariusvniekerk     |
| Katherine Kinnaman       | KK       | Anaconda      | kathatherine       |
| | | | |

11 people present


## Introductions


## Announcements


* (MRB, absent, please read out) Please remember to vote on adding Jaime to the steering council

* (MRB, absent, please read out) Please send comments on the new governance PR (https://github.com/conda-incubator/governance/pull/51)

* (JL) CEP 6 vote passed and implemenation is on the final stretch
    * https://github.com/conda-incubator/ceps/blob/main/cep-6.md

* (JL) Intention to call for vote for Code of Conduct proposal
    * https://github.com/conda-incubator/governance/pull/49
    * Steering Council Input still welcome!

* (JL) NEW! Public "planning" project board for some conda projects:
    * https://github.com/orgs/conda/projects/2
    * Single source of truth for Open Source efforts, including some agile ceremonies of the conda team at Anaconda
    * Open for feedback and hopefully improves visibility of priorities 
    * Covers a number of dimensions of project management:
        * issue sorting
        * support requests
        * backlog review
        * sprint planning
        * sprint review
        * documentation issues
        * epics
        * tentative roadmap plans

* (JL) NEW! CEP project board to track pull requests and issues:
    * https://github.com/orgs/conda-incubator/projects/1
    * Also accessible via https://github.com/conda-incubator/ceps/projects?type=beta

* (JL) Reminder: conda development sprint at SciPy 2022 in Austin July 16/17
    * focus on getting beginners to contribute
    * no need to commit to specific features or shipping code
    * informal event to talk about all things conda (and friends)

* (JL) New constructor community team
    * Formally transfers constructor, menuinst and conda-pack from "federated" to "community" project status. See governance policy for more info on ["federated projects"](https://github.com/conda-incubator/governance#community-federated--attic-maintenance)
    * New team consists of 10 members of the community
        * Ticket: https://github.com/conda-incubator/governance/issues/53
        * conda team: https://github.com/orgs/conda-incubator/teams/constructor/members
        * conda-incubator team: https://github.com/orgs/conda/teams/constructor/members
    * Goals are:
        * improve maintenance of these fundamental projects of the eco system
        * unblock contributions from community members (e.g. Jaime's work via Napari)
        * have a common code base for "installers" in the ecosystem 

* (JL) conda-zsh-completions moved to conda-incubator
    * Author esc reached out and asked to transfer it, thank you for years of maintenance!
        * https://twitter.com/esc___/status/1536702772128759809
    * Goal is to hand-over maintenance to community and align with other people interested in improved shell integration
    * New team with broader name "conda-completions":
        * https://github.com/orgs/conda-incubator/teams/conda-completions
    * May be realigned in future if plans for shell integration change
    * Contributors and feedback welcome!

## New Agenda Items

* (JK) Handling other shells ( https://github.com/conda/conda/issues/6820 )
    * Apple uses zsh by default on macOS
        * https://www.theverge.com/2019/6/4/18651872/apple-macos-catalina-zsh-bash-shell-replacement-features
    * Fish also sees a fair bit of usage
        * https://github.com/conda/conda/issues/7993

* (JL) Consolidating conda CLA information into conda/infra repo
    * https://github.com/conda/infra/issues/564

* (DPC) [Fiscal Sponsorship Proposal](https://github.com/conda-incubator/governance/issues/54)
    * Fiscal sponsorship allows us to accept funding and manage trademarks.  Creates conda as a legal entity
    * Submissions are due by July 15, which means we need input soon, so we can finish voting before that.

* (KK) [Conda capitalization](https://github.com/conda/conda-docs/issues/803)
   * If you care to comment, please do!
   * Main consensus currently is to follow what Git does. Git for organization/program, git for command

* (DH) [conda-package-streaming](https://github.com/conda-incubator/conda-package-streaming)
    * Coming soon
    * Downloads partial conda packages (both formats) for quick metadata inspection or any in-memory use
    * Byproduct of conda-index improvements

## What is this meeting for?

Various parts of the conda community gather on a regular basis.  This meeting brings together all of these sub-communities for a community wide call.