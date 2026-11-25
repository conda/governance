# Project Teams

- [Project Teams](#project-teams)
  - [Project Teams Details](#project-teams-details)
    - [Project Requirements](#project-requirements)
  - [Community Project Team Voting](#community-project-team-voting)
  - [Nominate new member of a Community Project Team](#nominate-new-member-of-a-community-project-team)
    - [Remove a Project Team Member](#remove-a-project-team-member)

## Project Teams Details

A Project Team is a [_sub-team_](../governance.md#sub-teams) with a [_dynamic_ charter](../governance.md#dynamic-charter), except for a few caveats as detailed here. They exist to maintain a specific project (or possibly set of projects). Each project in `conda` or `conda-incubator` should belong to exactly one Project Team. This team is granted write access to the repos associated with the project.

The initial Project Team for projects in the `conda` GitHub organization are specified in the [vote to move a project from the incubator to the main `conda` GitHub organization](../steering-council/charter.md#incorporate-a-software-project-into-the-main-conda-organization). As this vote has a 60% threshold and [sub-team formation](../steering-council/charter.md#sub-team-formation) is only a greater than 50% threshold, the vote for adding a project to the main `conda` GitHub organization can serve both purposes. Project Teams for incubating projects do not need a vote for their creation. Instead they are created [when the project is moved into `conda-incubator`](../governance.md#incubation).

For [_federated_](../governance.md#federated-projects) and [_incubating_](../governance.md#incubation) projects, the Project Team decides among themselves on how to add and/or remove members from the Project Team. Further, Project Teams for incubating projects are exempted from the requirement to have at least one Steering Council member. For federated projects, the Project Team must have at least one Steering Council member. For a [_community maintained project_](../governance.md#community-projects), a petition for commit rights is made to the current members of the Project Team for that project. If this petition passes according to the voting rules for [Nominate new member of a Project Team](../project-team/charter.md#nominate-new-member-of-a-community-project-team) below, the petitioner is granted write access and added to the team.

### Project Requirements

All projects must prominently list their maintenance status in their README and provide clear instructions on where people can seek help for the project. The possible maintenance statuses are one of [`federated`](../governance.md#federated-projects) or [`community`](../governance.md#community-projects) or [`archive`](../governance.md#archive-projects).

**All conda projects must use an [OSI approved software license](https://opensource.org/).** We recommend and encourage the use of [BSD-family licenses](https://opensource.org/licenses/BSD-3-Clause). We recommend that specifications and documentation use [Creative Commons licenses](https://creativecommons.org/).

[Project Teams](#project-teams) decide among themselves whether or not to move their projects in and out of `archive` status. The Steering Council must be notified before this change and will move `archive` projects to the `conda-archive` organization and mark them as archived.

## Community Project Team Voting

Here are the minimal voting policies for Community Project Teams.

For the meaning of **Sensitive** and the general rules on abstentions, voting periods, and AoE deadlines, see the [Voting documentation](../steering-council/charter.md#voting). Participation and approval requirements for Project Team votes are specified below.

## Nominate new member of a Community Project Team

The proposer must provide a sufficient justification as to why the nominee should be welcomed into the Project Team. Prior work on the project is an essential part of the nomination process. The voting body for these votes are the current members of the Project Team at the time the nomination is made.

- Sensitive
- Voting: One of the following:
  - at least 3 members voting, with all votes being "yes"
  - at least 50% participation, with greater than 50% "yes" votes to pass

### Remove a Project Team Member

Sufficient justification must be given as to why a Project Team member should be removed. Removing a Project Team member who was added by the Steering Council via the [Project Team Membership Appeal](../steering-council/charter.md#project-team-membership-appeal) process may be considered a violation of the Code of Conduct if sufficient justification is not given.

- Sensitive
- Voting:
  - At least 50% participation
  - More than 50% "yes" votes to pass
