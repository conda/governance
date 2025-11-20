from typing import Literal
from pydantic import BaseModel, HttpUrl, ConfigDict, Field


class Scopes(BaseModel):
    """
    Defines the responsibilities of a Conda sub-team.
    This structure is nested within the main CondaSubTeam model.
    """

    model_config = ConfigDict(extra="forbid")

    codeowners: list[str] | None = ...
    """The GitHub projects this team owns or has write access to."""

    other: list[HttpUrl] | None = ...
    """Other responsibilities of this team"""


class CondaSubTeam(BaseModel):
    """
    Model for defining Conda Sub-Teams based on the governance structure.
    """

    model_config = ConfigDict(title="Conda Sub-Teams", extra="forbid")

    name: str = ...
    """The team name in GitHub"""

    description: str = ...
    """The team description in GitHub"""

    charter: Literal["dynamic", "static", "project"] = ...
    """
    The team charter type, see [dynamic](https://github.com/conda/governance#dynamic-charter),
    [static](https://github.com/conda/governance#static-charter),
    and [project](https://github.com/conda/governance#project-teams-details) requirements.
    """

    requirements: str | None = ...
    """Special requirements for team membership"""

    scopes: Scopes = ...
    """Team responsibilities"""

    links: list[HttpUrl] = ...
    """Important links, e.g. the issue/PR proposing the team creation"""

    members: dict[str, HttpUrl | None] = Field(..., min_length=1)
    """Maps username to a record of the decision adding them to the team"""

    emeritus: dict[str, HttpUrl | None] | None = Field(..., min_length=1)
    """Maps username to a record of the decision removing them from the team"""


if __name__ == "__main__":
    import json
    from pathlib import Path

    schema = CondaSubTeam.model_json_schema()
    (Path(__file__).parents[1] / "teams" / "teams.schema.json").write_text(
        json.dumps(schema, indent=2)
    )
