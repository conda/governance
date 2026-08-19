# /// script
# dependencies = [
#   "pydantic>=2,<3",
# ]

from typing import Annotated, Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    HttpUrl,
)


class Resources(BaseModel):
    """
    Defines the responsibilities of a Conda sub-team.
    This structure is nested within the main CondaSubTeam model.
    """

    model_config = ConfigDict(extra="forbid", use_attribute_docstrings=True)
    teams: (
        list[
            Annotated[
                str, Field(pattern=r"[a-zA-Z0-9\-_\.\+]{1,128}/[a-zA-Z0-9\-_]{1,128}")
            ]
        ]
        | None
    ) = ...
    "The Github team (or teams, across different organizations) representing this team."
    repos: (
        list[
            Annotated[
                str,
                Field(pattern=r"[a-zA-Z0-9\-_\.\+]{1,128}/[a-zA-Z0-9\-_\.\+]{1,128}"),
            ]
        ]
        | None
    ) = ...
    """The GitHub repositories this team owns or has write access to."""
    other: list[HttpUrl] | None = ...
    """Other responsibilities of this team"""


class MemberDetails(BaseModel):
    """
    Defines the contact details of a team member.
    """

    model_config = ConfigDict(extra="forbid", use_attribute_docstrings=True)

    full_name: str | None = ...
    """Full name of the member."""
    email: EmailStr | None = ...
    """Email address of the member."""
    funder: str | None = ...
    """Employer or sponsor for the time allocated to the project."""
    pronouns: str | None = ...
    """Pronouns of the member."""
    decision: HttpUrl | list[HttpUrl] | None = ...
    """URL pointing to the record of the membership decision"""


class CondaSubTeam(BaseModel):
    """
    Model for defining Conda Sub-Teams based on the governance structure.
    """

    model_config = ConfigDict(
        title="Conda Sub-Teams", extra="forbid", use_attribute_docstrings=True
    )

    name: str = Field(..., pattern=r"[a-zA-Z0-9\-_]{1,128}")
    """The team name as per the governance (no organization name!)."""

    description: str = Field(..., min_length=0, max_length=255)
    """The team description in GitHub"""

    charter: Literal[
        "council",
        "dynamic-subteam",
        "static-subteam",
        "community-project",
        "federated-project",
        "unknown",
    ] = ...
    """
    The team and charter type, see [dynamic](https://github.com/conda/governance#dynamic-charter),
    [static](https://github.com/conda/governance#static-charter),
    and [project](https://github.com/conda/governance#project-teams-details) requirements.
    """

    details: str | None = ...
    """
    Additional documentation for the team (membership requirements, responsibilities,
    onboarding guides, escalation procedures, etc) or a reference to the location
    where such information is discussed.
    """

    resources: Resources = ...
    """Resources owned by the team (Github teams, repos, service accounts, etc)"""

    links: list[HttpUrl] = ...
    """Important links, e.g. the issue/PR proposing the team creation"""

    members: dict[str, MemberDetails | HttpUrl | None] = ...
    """
    Maps username to its details or, in its simplified form, a URL pointing
    to the record of the decision adding them to the team.
    """

    emeritus: dict[str, MemberDetails | list[HttpUrl] | HttpUrl | None] | None = ...
    """
    Maps username to its details or, in its simplified form, a URL pointing
    to the record of the decision removing them from the team.
    """


if __name__ == "__main__":
    import json
    from pathlib import Path

    schema = CondaSubTeam.model_json_schema()
    (Path(__file__).parents[1] / "teams" / "teams.schema.json").write_text(
        json.dumps(schema, indent=2) + "\n"
    )
