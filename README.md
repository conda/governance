- [Conda & Conda-Incubator Governance](#conda--conda-incubator-governance)
  - [Code of Conduct](#code-of-conduct)
  - [Naming & Manifest](#naming--manifest)
  - [Terminology](#terminology)
  - [Teams & Roles](#teams--roles)
    - [Steering Council](#steering-council)
    - [Project Teams](#project-teams)
    - [External Contributors](#external-contributors)
    - [Emeritus Steering](#emeritus-steering)
  - [Sub-Teams](#sub-teams)
    - [Dynamic Charter](#dynamic-charter)
    - [Static Charter](#static-charter)
  - [Community, Federated & Attic Maintenance](#community-federated--attic-maintenance)
    - [Community Projects](#community-projects)
    - [Federated Projects](#federated-projects)
    - [Attic Projects](#attic-projects)
    - [Project Requirements](#project-requirements)
    - [The Rationale for Federated Projects](#the-rationale-for-federated-projects)
  - [Trademarks](#trademarks)
  - [Incubation](#incubation)
  - [Project Teams Details](#project-teams-details)
  - [Steering Council Membership](#steering-council-membership)
    - [Steering Council Size](#steering-council-size)
    - [Provisional Members](#provisional-members)
  - [Shared Funding Membership restrictions](#shared-funding-membership-restrictions)
    - [Shared Funding: Proximate, Ultimate, and In Between](#shared-funding-proximate-ultimate-and-in-between)
      - [Tracking Funding](#tracking-funding)
  - [Steering Council and Project Teams Interactions](#steering-council-and-project-teams-interactions)
    - [Community Project Teams must be open to qualified new members](#community-project-teams-must-be-open-to-qualified-new-members)
  - [Voting](#voting)
    - [Posting results](#posting-results)
    - [Quorum](#quorum)
    - [Voting Total Examples](#voting-total-examples)
  - [Voting items](#voting-items)
    - [Enhancement Proposal Approval](#enhancement-proposal-approval)
    - [Nominate new Steering Council member](#nominate-new-steering-council-member)
    - [Nominate a Provisional Steering Council Member](#nominate-a-provisional-steering-coiuncil-member)
    - [Remove a Provisional Steering Council Member](#remove-a-provisional-steering-council-member)
    - [Resolve Overlapping Funding](#resolve-overlapping-funding)
    - [Sub-team Formation](#sub-team-formation)
    - [Sub-team Dissolution](#sub-team-dissolution)
    - [Add Project/Repo to Incubator](#add-projectrepo-to-incubator)
    - [Remove Project/Repo from Incubator](#remove-projectrepo-from-incubator)
    - [Incorporate a Software Project into the main `conda` Organization](#incorporate-a-software-project-into-the-main-conda-organization)
    - [Lock an Issue, Pull Request, Thread](#lock-an-issue-pull-request-thread)
    - [Block a Contributor](#block-a-contributor)
    - [Remove a Steering Council member](#remove-a-steering-council-member)
    - [Spending of funds](#spending-of-funds)
    - [Modifying the governance document](#modifying-the-governance-document)
    - [Project Team Membership Appeal](#project-team-membership-appeal)
    - [All Other Items](#all-other-items)
    - [Community Project Team Voting](#community-project-team-voting)
      - [Nominate new member of a Community Project Team](#nominate-new-member-of-a-community-project-team)
      - [Remove a Project Team Member](#remove-a-project-team-member)
  - [Current Steering Council Members](#current-steering-council-members)
  - [Emeritus Steering members](#emeritus-steering-members)
  - [Document History](#document-history)


# Conda & Conda-Incubator Governance

This document outlines the policies and procedures that manage the conda community. This document recognizes that, while packaging and package tooling is deeply important to all of us, participation in the organization is voluntary. Individual members of the Steering Council, any sub-team, and external contributors choose to participate and may choose to leave at any time for any reason or for no reason.

Larger organizations, such as for-profit businesses, that contribute code and support to the conda organization are welcome to (but not required to) [maintain creative control](#federated-projects) of their contributions as long as such contributions adhere to the rules in this document. Such organizations are also welcome to [cede creative & maintenance control](#community-projects) of any specific project to the community as well.

We deeply appreciate all good faith contributions.

## Code of Conduct

The conda Organization's [Code of Conduct](CODE_OF_CONDUCT.md) governs all interactions within the conda Organization.  Please take a few minutes to familiarize yourself with it.

## Naming & Manifest

This document defines the conda Organization as the body responsible for governing the tools, specifications, and libraries within the conda ecosystem, broadly speaking. This encompasses specific GitHub organizations, such as [`conda`](https://github.com/conda/) and [`conda-incubator`](https://github.com/conda-incubator/). Authors of particular software projects, such as [`conda`](https://github.com/conda/conda) or [`mamba`](https://github.com/mamba-org/mamba), are free to choose if and when their projects are included as part of the conda Organization.

This organization does not hold as part of its role the creation of any packages. The act of packaging itself has other organizations dedicated to their creation, such as [Anaconda](https://anaconda.com/), [conda-forge](https://conda-forge.org/), and [bioconda](https://bioconda.github.io/).

## Terminology

1. *conda* or *the conda Organization* : The conda Organization defined here, including `conda` and `conda-incubator`.
2. *The [conda project](https://github.com/conda/conda)* : The actual conda software itself, as distinct from the conda Organization.
3. *The conda ecosystem* : The broadest set of tools, packages, and people that use any conda related tooling. The conda Organization is a subset of *the conda ecosystem*. Members of the ecosystem should not feel compelled or obligated to participate in the conda Organization, though positive engagement is welcome.

## Teams & Roles

The primary teams participating in the conda Organization's activities are:

### Steering Council

The Steering Council is the governing body over the entire conda Organization. Members of the Steering Council have full voting rights within the organization. Steering Council members are the face of the organization, and are responsible for officially interfacing with external communities, organizations, non-profits, and companies. The Steering Council may create new sub-teams, as appropriate. Each Steering Council member is entitled to one vote on all elected matters.

### Project Teams

Project Teams are responsible for the management of a software project consisting of one or more repositories and any software releases. Project Team members have the ability to merge pull requests into the repositories of the software project they maintain and produce releases of that software project. See the [Project Teams Details](#project-teams-details) section for more.

### External Contributors

This group encompasses all others who are not on the Steering Council or Project Teams. This includes first-time contributors, collaborators, and original authors. They have no special rights within the conda organization itself.

### Emeritus Steering

[Steering Council](#steering-council) members that are inactive (commits, GitHub comments/issues/reviews, dev meetings, and voting on polls) in the past six months will be asked if they want to become Emeritus Steering members. One week after asking, if the inactive Steering Council member has not responded, they will be automatically moved to emeritus status. Any Steering Council member can also request to become Emeritus if they wish to do so (e.g. taking a sabbatical or long vacation). Emeritus Steering members can be brought back to active Steering Council membership at anytime, assuming there is space and no other policies (e.g., shared funding, council size, etc.) are violated. Emeritus Steering Council members cannot vote. The [`steering.csv`](steering.csv) list should be updated when change in the status of a member occurs with the member added to the [`emeritus.csv`](emeritus.csv) file.

## Sub-Teams

The [Steering Council](#steering-council) may elect to create new sub-teams for managing the daily business of the organization. While sub-teams may have non-Steering members, **every sub-team must have at least one [non-provisional](#provisional-members) Steering Council team member at all times.** If a sub-team fails to have a Steering Council member for more than 1 week, that team is considered to be dissolved. A new sub-team would need to be established by the Steering Council in order to reinstate the activity.

All sub-teams must adhere to the governance, policies, and procedures of the conda Organization at all times. Sub-teams have a charter that is either *dynamic* or *static*.

### Dynamic Charter

A **dynamic** charter means that the sub-team is self-organizing, with respect to its own internal policies, procedures, and membership. A sub-team may choose to modify its membership independent of the Steering Council. For example, a Google Summer of Code team could be a good candidate for a dynamic charter. Project Teams also have a dynamic charter.

### Static Charter

A **static** charter means that all membership decisions and non-trivial policy changes must be approved by the Steering Council. For example, a finance team may require a static charter.

## Community, Federated & Attic Maintenance

The conda Organization acknowledges that project contributions may come from a variety of sources. To this end we define three maintenance categories for our projects.

### Community Projects

A **Community** maintained project is one where the development, ownership, and maintenance are controlled by the conda Organization at large. Contributors keep the copyright for code they wrote and submit for inclusion to the respective project under the terms of license of that project.

### Federated Projects

A **Federated** project is maintained by a sub-team of *the conda Organization*. Such projects maintain control of distribution and licensing via the project's sub-team. Federated projects are not controlled by the community at large. Still, as part of the conda Organization, federated projects agree to the terms of this governance document, including but not limited to the [Code of Conduct](CODE_OF_CONDUCT.md).  See the [The Rationale for Federated Projects](#the-rationale-for-federated-projects) section below for more.

### Attic Projects

An **Attic** project is one which is unmaintained or clearly superseded by another project. No support is provided or anticipated for these projects.

### Project Requirements

All projects must prominently list their maintenance status in their README and provide clear instructions on where people can seek help for the project. The possible maintenance statuses are one of `federated` or `community` or `attic`.

All conda projects must use an [OSI approved software license](https://opensource.org/). We recommend and encourage the use of [BSD-family licenses](https://opensource.org/licenses/BSD-3-Clause). We recommend that specifications and documentation use [Creative Commons licenses](https://creativecommons.org/).

[Project Teams](#project-teams) decide among themselves whether or not to move their projects in and out of `attic` status. The Steering Council must be notified before this change and will mark `attic` projects as archived.

### The Rationale for Federated Projects

[Federated projects](#federated-projects) enable conda ecosystem projects to exist under the same umbrella organization, while maintaining community standards. They acknowledge the time and investment the developers and authors have put into their creations and that in certain cases they wish to maintain creative control. A federated system also allows for a phased transition plan for projects to become increasingly community maintained over time.

Federated projects cannot expect that the community will maintain or support the project as long as the project remains federated. If/when a federated project transitions to the community maintenance model, this project will be maintained and supported by the community.

Federated projects are under no obligation to have a transition plan or any intention of becoming a community maintained project. However, this is strongly encouraged and community maintained projects are seen as the ideal. Federated projects are seen as the reality.

## Trademarks

[Community Projects](#community-projects) need to license/assign the project's trademarks when becoming a conda Organization Community Project. This is an act of good faith and communicates to the community that the project are committed to our overall efforts.

1. Trademarks are irrevocably *licensed or transferred* to the conda Organization's fiscal sponsor when a project is added to the conda Organization as a Community Project.
2. The conda Organization, in conjunction with our fiscal sponsor, then have the right to sublicense the trademarks to other projects, subject to specific limitations: The conda Organization may not degrade the distinctiveness of *licensed* trademarks, or use *licensed* trademarks to disparage or misrepresent the assigner. *Transferred* trademarks are completely controlled by the conda Organization and its fiscal sponsor.
3. The [Steering Council](#steering-council) then makes trademark decisions, subject to agreed upon restrictions, and coordinates efforts with our fiscal sponsor.

We have guidelines for making decisions about conda Organization trademarks:

1. The project should be open source with a permissive license
1. The project should be related to the conda ecosystem
1. The project should be not be overly grand in claiming namespace
1. The project should not make subjective claims in the chosen project name

Examples of project names that violate the 3rd and 4th guidelines are `conda Pro`, and `pets-dot-com-conda-saves-the-day`.

The conda Organization is in a particularly challenging situation here because the conda name and logo are obviously derived from the [Anaconda Inc.](https://anaconda.com/) name and logo. Several precedents guide us here: Projects like [conda-forge](https://conda-forge.org/) (name), [Bioconda](https://bioconda.org/) (name and logo) and [conda-lock](https://github.com/conda-incubator/conda-lock) (name) have been approved in the past.


## Incubation

All projects start their journeys in an experimental or unstable state. To this end, we delineate stable projects as living in the [`conda` GitHub organization](https://github.com/conda/). Therefore, projects new to the conda Organization and governance must begin their inclusion in the [`conda-incubator` GitHub organization](https://github.com/conda-incubator/). The barrier to entry for a project to be added to the incubator should be very low. A vote from the [Steering Council](#steering-council) is required to move a project from incubation to the main GitHub organization.

Any single member of the Steering Council may add a project to the incubator, given the knowledge and consent of the author(s) (see [below](#voting)). Members of the Steering Council that are sponsoring the incubation are responsible for ensuring that basic legal requirements have been met that allow for the incubation. For example, [trademark usage and license terms](#trademarks) must been checked prior to incubation.

## Project Teams Details

A Project Team is a sub-team with a dynamic charter, except for a few caveats as detailed here. They exist to maintain a specific project (or possibly set of projects). Each project in `conda` or `conda-incubator` should belong to exactly one Project Team. This team is granted write access to the repos associated with the project.

The initial Project Team for projects in the `conda` GitHub organization are specified in the vote to move a project from the incubator to the main `conda` GitHub organization. As this vote has a 60% threshold and sub-team formation is only a greater than 50% threshold, the vote for adding a project to the main `conda` GitHub organization can serve both purposes. Project Teams for incubating projects do not need a vote for their creation. Instead they are created when the project is moved into `conda-incubator`.

For [federated](#federated-projects) and [incubating](#incubation) projects, the Project Team decides among themselves on how to add and/or remove members from the Project Team. Further, Project Teams for incubating projects are exempted from the requirement to have at least one Steering Council member. For federated projects, the Project Team must have at least one Steering Council member. For a community maintained project, a petition for commit rights is made to the current members of the Project Team for that project. If this petition passes according to the voting rules for "[Nominate new member of a Project Team](#nominate-new-member-of-a-community-project-team) below, the petitioner is granted write access and added to the team.

## Steering Council Membership

Steering Council members need to 1) be invested in the conda ecosystem and community, and 2) have time and energy to contribute to conda Organization governance.  Council members, with the exception of [provisional members](#provisional-members), will have a demonstrated record of prior service to the conda community.

### Steering Council Size

The Steering Council should reflect a wide range of interests, and still be small enough to have a reasonable expectation that [quorum requirements](#quorum) can be met when votes are called.

The minimum and maximum sizes for the Steering Council are:

* Minimum: 9
* Maximum: 21

The minimum of 9 works well with the [minimum quorum size of 5](#quorum) specified below. The maximum of 21 allows for a diversity of members, including as many as 7 Provisional Members (see below), and representation from 11 to 21 different participating organizations (see below).

If the Steering Council falls below its minimum, then all other Council business is suspended until this requirement is met. The only allowed council actions, in this case, are votes on adding Provisional members, votes on adding new contributing members, votes to resolve overlapping funding, existing members moving to Emeritus status, or existing members coming back from Emeritus status.

If the Steering Council membership exceeds its maximum, then all other Council business is suspended until this requirement is met. The only allowed council actions, in this case, are votes on removing Provisional members, votes on removing contributing members, votes to resolve overlapping funding, existing members moving to Emeritus status, or existing members coming back from Emeritus status.

No vote can be held that would push the Steering Council above its maximum size if the vote resulted in adding either standard or provisional Steering Council members.

### Provisional Members

As mentioned above, Steering Council members will usually have a demonstrated record of prior service to the conda community.  This requirement works well for ensuring that Council members are invested in the community before they can become part of community governance.

We also want to encourage participation by commercial and grant funded organizations that have committed to investing in the conda ecosystem. To encourage these organizations to commit resources to the conda ecosystem, **Provisional Steering Council Memberships** are available.

Provisional memberships are open to organizations that have committed resources to the conda Organization, but do not yet have an established record of contribution *within* the conda Ecosystem. Provisional memberships encourage investment, and give investing organizations an immediate voice in community decisions.

Provisional memberships are open to organizations that

* Are funding at least one FTE contributing to the conda ecosystem
* Have not demonstrated a record of prior service to the conda community

These organizations can request 1 provisional membership on the Steering Council. The evaluation criteria for evaluating this request is based on the organization’s and the nominated person’s commitment to open source principles *as demonstrated in other projects.*

Provisional memberships are expected to be temporary, lasting just long enough for contributors from that organization to demonstrate their values and earn representation as individual contributors.

Provisional memberships can also be revoked at any time by a simple majority vote of the Steering Council, if and when the Council determines that the organization or the individual is no longer acting in the larger interests of the conda community.

Finally, **no more than 1/3 of the Steering Council membership can be Provisional Members.** At all times, at least 2/3 of the Steering Council membership hold a seat because of demonstrated contributions to the conda ecosystem. If this threshold is violated then all other Council business is suspended until this requirement is met. The only allowed actions, in this case, are votes on removing Provisional members, votes on adding new contributing members, votes to resolve overlapping funding, existing members moving to Emeritus status, or existing members coming back from Emeritus status.

## Shared Funding Membership restrictions

**No more than 2 council members can have the same funder:**  Each Steering Council member can have the same funding organization as **at most one other Council member.**

The conda Organization [actively encourages](#provisional-members) participation by commercial entities.  However, we also need to preserve the voices of individual contributors, and prevent the conda Organization from ever favoring the financial interests of any commercial entity over the interests of the larger community.

The conda Organization enforces this restriction by tracking the funding sources of each Steering Council member.

### Shared Funding: Proximate, Ultimate, and In Between

Funding can be multilayered and complicated.

For example, Robert is a researcher in the Computer Science department at Western Michigan University and is working on a National Science Foundation (NSF) grant. For the purposes of the conda Organization, is Robert’s funder his CS department, the university, the specific grant, a division of NSF, the NSF, the US government, or all of the above?

Meanwhile, across the world, Gouri works for GitHub, San-Yih works for LinkedIn, and João works on VS Code. Do they work for separate funders, or are they all funded by Microsoft?

We use this guideline for determining which level(s) of funding to use for membership eligibility:

> **When determining if funding is shared, choose the broadest level of funding where people might have a common set of goals because of their shared funding source.**

In Robert’s situation, two levels are good candidates for determining shared funding.

1. If Robert, or Robert’s department, is widely involved in many aspects of the conda ecosystem, then we may want to include his department in the list of Robert’s funders.
2. If Robert is working on a grant that spans many universities then we may want to include the grant.

In most circumstances we will not include the university as a funder because projects in the CS department, and in the Economics department, for example, are unlikely to have shared interests driven by both being at the same university. People funded by NSF, divisions of NSF, or the US government are also unlikely to have shared interests that are driven by their shared funding.

In the other example, Microsoft is a large company and these three largely unrelated parts of it are unlikely to have common goals based mainly on their common ultimate funder. However, a company that wanted to control the conda Organization could do so by enlisting people from across their organization, claim separate funding, and then capture the council. **In this case, the default guideline is to treat all parts of a company as having one funder.**

#### Tracking Funding

Nominated members will provide a list of organizations that fund above 25% of their time. Nominees will need to provide a complete “chain of funding” for each funding source. For example: “GitHub, a part of Microsoft”, or “CS Dept at Western Michigan University, *Computational Reproducibility Made Easy grant*, NHGRI, NIH, US Federal Government.”

The Steering Council determines the appropriate funding level(s) to consider when looking for common funding with existing and proposed members. The funding source of any Steering Council member can be put to a vote under the policy for [All Other Items](#all-other-items) below.

Council members need to keep their funding documentation up to date, and notify the council whenever it changes. Should a change in funding state create a shared funding situation, the council members should decide who among themselves should move to emeritus status. If no agreement can be reached, the Steering Council will hold a simple vote to determine which member is moved to emeritus status under the [Resolve Overlapping Funding](#resolve-overlapping-funding) voting provision below.

In cases where people have absolutely no funding related to conda, we still document this funding state, but we do not require people to list their (irrelevant) funding. The "no funding" state can be held by an unlimited number of Steering Council members.

## Steering Council and Project Teams Interactions

The Steering Council and the Project Teams have different roles and different motivations. conda governance aims to impose just enough oversight of Project Team procedures to ensure that membership and voting are indeed open and fair.

### Community Project Teams must be open to qualified new members

Community projects must be open to new members who demonstrate their capability and interest in the project through working with the project as a contributor first. If an application to join a Community project is rejected, the person can appeal to the Steering Council. If the rejected person can prove that they in fact meet the criteria for becoming a Project Team member and that they were rejected for inappropriate reasons, including their funding source, then the rejection will be overturned. This voting item falls under the [Project Team Membership Appeal](#project-team-membership-appeal) policy below.

It is possible that a project joins as a Community Project, but in fact not be committed to open source principles. If they consistently reject qualified “outside” applicants for Project Team membership, then Steering Council review could lead to a gradual shift in Project Team membership, and causing the original team members to leave.

We minimize the chance of this happening by clearly communicating requirements for Community Projects when bringing in a new project.

Note that [Federated](#federated-projects) and [Incubator](#incubation) projects are not required to be open to new membership.

## Voting

This section presents descriptions and criteria for voting items in the conda Organization. The [Steering Council](#steering-council) is the only team with voting rights at the conda Organization level. Steering Council members may also call a vote on any topic. The restrictions on calling a vote are as follows:

* There must only be one vote active on a particular item at any time.
* The act of calling for a vote must not itself violate the code of conduct. For example, Sam repeatedly called for votes immediately after a previous vote failed to achieve Sam's result. Sam is attempting to bully other Steering Council members into agreeing, and is thus violating the code of conduct.
* Voting yes moves the proposal forward;
  Voting no is the only way to express opposition to the proposal;
  There is always an option to abstain from voting;
  Not voting is discouraged, but non-votes do not count as "no", "yes", or "abstain".
* Steering Council members must explicitly abstain from a vote via making a comment on the PR/issue or selecting the "abstain" option. Simply not voting at all doesn't count as an abstention.
* Abstentions count towards the [quorum](#quorum) but are excluded when computing if a vote passes.

Voting items are labeled as either **standard** or **sensitive**. Standard items are ones where public record and discourse is preferable. Sensitive voting items are ones where the results of the vote should remain private to the voters after the vote has occurred. Sensitive votes should take place on a secure anonymous voting platform in order to retain election integrity and anonymity. (We may use [`Polys`](https://polys.me) and the [`Helios voting system`](https://vote.heliosvoting.org/), but are open to any secure, anonymous system.) The email capability of your chosen voting platform should be used for sending voting invitations and reminders if possible. All votes should be sent to the appropriate people using their email listed in `steering.csv` as applicable.

The default voting period is 1 week (7 days). This may be modified at the time when a vote is called, but may never be less than one week modulo exceptions for some time-sensitive votes below.

Additional requirements may apply in case low turnouts have to be handled, see "[quorum](#quorum)" below.

To call for a standard vote, here is a template Issue/PR comment:

    @conda/stering
    This PR falls under the {policy} policy, please vote and/or comment on this PR.
    This PR needs {policy_percent} of the Steering Council to vote yea to pass.
    To vote please leave Approve (yea) or Request Changes (nay) reviews.
    If you would like changes to the current language please leave a comment or push to this branch.
    This vote will end on {date}.

A `vote` label must be applied to the PR or issue.

### Posting results

To maintain the historical record, the outcome of any standard vote which invoked the timeout rules below should be recorded in the [`vote-results`](vote-results/) folder of our documentation.

Each "timed out" vote should be its own file.  The filename should reflect the topic and the date that the vote opened. The file should contain at least:

* vote description
* vote policy
* vote totals
* Poll open and close dates
* documentation of the vote reminders as detailed below

Non-timed-out vote results should be documented in github PR/issue upon which the voting happened. A `vote` label must be applied to the PR or issue.

### Quorum

With one exception, all percentages below express *both* required participation, as a fraction of active Steering Council members, as well as the fraction of those who vote affirmatively (i.e. vote `yes`) on the issue. The fraction of those who voted affirmatively is determined from the total number who voted `yes`, `no` or `abstain`, not the size of the active Steering Council. The exception is when 50% is required. In these cases, *at least half* of team members need to participate, but *more than 50%* of votes need to be affirmative for the vote to pass. Some votes have special quorum rules and those are listed explicitly below.

For example, in a vote requiring 50% participation, with 20 active members, at least 10 must vote; if 10 or 11 vote, there must be at least 6 affirmative votes. If 12 or 13 members vote, at least 7 votes must be affirmative to pass, and so on.

To prevent any [funding organization](#shared-funding-membership-restrictions) from swaying the majority of votes on any topic, the minimum quorum for a vote must be at least 5 members, or the specified council membership percentage for this type of vote, whichever is greater.

Because everyone is busy and it is difficult sometimes to get quorum, votes not achieving quorum will eventually time out on their set end date. When this happens, the current participation level is taken for what it is, and the percentage of affirmative votes is calculated from whatever the vote total is at that time. In order for a timeout to occur, the vote must have:

* met the minimum quorum described above
* been open for at least 2 weeks
* been presented and discussed at a Steering Council meeting
* been advertised on at least 3 separate occasions on the Steering Council chat channel (beginning of voting period, middle, and one day prior to proposed timeout)
* been sent to Steering Council members via email. Email reminders must have been sent similarly to the Steering Council chat channel: at least 3 times, occurring as beginning of voting period, middle, and one day prior to proposed timeout.

Extending the above example, if 9 people are required for a quorum, but only 7 have voted, those 7 votes can form the basis of a completed vote after the above conditions are met. 4 votes within those 7 would be needed to pass the vote.

To post a timeout reminder, here is a template comment:

    @conda/steering
    This vote falls under the {policy} policy, please vote and/or comment on this PR.
    This vote needs {policy_percent} of the Steering Council to vote yea to pass.
    This vote presently has {current_voters}, and needs {policy_percent * steering_council - current_voters} more for quorum.
    It is proposed that this vote will time out and be evaluated with the current votes in {days}, on {date}.
    To vote please leave Approve (yea) or Request Changes (nay) reviews.

To declare a standard vote "timed out," the person making such a declaration must post a pull-request adding a vote record to the [`vote-results`](vote-results/]) folder. The declaration PR should be merged by the first Steering Council member who is available to verify that the requirements for the timeout have been met, based on their own personal records.

### Voting Total Examples

Assume the Steering Council has 10 active members and the vote threshold is 50%.

1. Among Steering Council members there are 3 "yes", 2 "no", and 1 "abstain" votes. This vote has reached quorum (3 + 2 + 1 = 6 which is at least 50% of 10). It also passes since it recorded 3 "yes" votes and 2 "no" votes giving 3/5 (60%) which is greater than 50% of 5.

2. Among Steering Council members there are 4 "yes", 3 "no", and no abstentions. This vote has reached quorum (4 + 3 = 7 which is at least 50% of 10). It has also passed since it recorded 4 "yes" votes and 3 "no" votes giving 4/7 which is greater than 50% of 6.

3. Among Steering Council members there are 3 "yes" votes, "1" no vote and no abstentions. Further the timeout rules above **were** invoked. This vote has thus reached quorum and it has passed since 3/4 (75%) is greater than 50%.

4. Among Steering Council members there are 3 "yes" votes, "1" no vote and no abstentions. Further, the timeout rules above **were not** invoked. This vote has not reached quorum and should be extended or redone.

## Voting items

### Enhancement Proposal Approval

When ready, the proposer may call for a vote on an existing [conda enhancement proposal (CEP)](https://github.com/conda-incubator/ceps). This requires a super-majority (60%) to pass so that the decision to accept the CEP is unequivocal and we have ensured that consensus has been reached.

* Standard
* 60% Majority to pass

### Nominate new Steering Council member

The proposer must provide a sufficient justification as to why the nominee should be welcomed into the Steering Council. Prior service to the community, including but not limited to: working on conda organization projects, writing conda specifications, and helping to bridge disparate communities are an important part of the nomination process.

* Sensitive
* 2/3rds Majority to pass

### Nominate a Provisional Steering Council Member

The proposer must provide a sufficient justification as to why the nominee should be welcomed on a provisional basis into the Steering Council. The guidelines on [Provisional Members](#provisional-members) must be followed as well.

* Sensitive
* Voting:
  * At least 50% participation
  * More than 50% "yes" votes to pass

### Remove a Provisional Steering Council Member

The proposer must provide a sufficient justification as to why the provisional member should be removed. The guidelines on [Provisional Members](#provisional-members) must be followed as well.

* Sensitive
* Voting:
  * At least 50% participation
  * More than 50% "yes" votes to pass

### Resolve Overlapping Funding

In the case that more than two Steering Council members share the same funding source and no agreement can be reached
amoung the members with shared funding as to who will enter emeritus status, the Steering Council will hold a simple
plurality vote in order to resolve the funding conflict. Each member with shared funding will be listed as a separate option in the
vote. The Steering Council will then vote on which member should be moved to emeritus status. The member who receives the most votes is moved to emeritus status. The quorum for this vote is five. In the case of a tie, the member is chosen at random.

* Sensitive
* Voting:
  * Simple plurality of votes
  * Member with most votes is moved to emeritus status
  * Ties are resolved by choosing a member at random
  * The quorum for this vote is five votes

### Sub-team Formation

Proposers must specify the name, role & responsibility, members, and charter (dynamic or static) of any new sub-teams.

* Standard
* Voting:
  * At least 50% participation
  * More than 50% "yes" votes to pass

### Sub-team Dissolution

Proposers must specify the name and justification for why a sub-team should be dissolved.

* Standard
* Voting:
  * At least 50% participation
  * More than 50% "yes" votes to pass

### Add Project/Repo to Incubator

Any single Steering Council member may add a project to the incubator, given the knowledge and consent of the author(s). The low barrier to entry here is because we want to encourage innovation, experimentation, and growth.  Steering Council members are encouraged to use common sense when adding new projects to the `conda-incubator` organization.

* Standard
* 1 Steering Council member willing to add the repository, no vote required

### Remove Project/Repo from Incubator

While we do not anticipate this ever being necessary, if the situation arises where a project needs to be removed from the incubator, two potential options are available, depending on the copyright and maintenance of the project.

In the first, easy case, the incubated project has been wholly developed and maintained by the authors. Here, the project should be allowed to leave incubation if the developers of that project decide and consent to leave. No vote from the Steering Council is required. A willing Steering Council member may be needed to transfer the repository, though.

In the second case, the incubated project has been communally developed by other members of the conda organization AND/OR the copyright of the project has been transferred to the conda organization, NumFOCUS, or a similar entity that is larger than the developers/copyright holders at the time of initial incubation.  In this case, the Steering Council must decide whether or not to allow the project to leave. A simple vote is required.

* Standard
* Voting:
  * At least 50% participation
  * More than 50% "yes" votes to pass

### Incorporate a Software Project into the main `conda` Organization

At some point, many projects will want to be included in the main `conda` GitHub (or otherwise) organization. Moving a project into this organization can be done with a super-majority vote from the Steering Council. There are no strict criteria for when a project is ready, stable, or viable for this step. Rather, Steering Council members are entrusted to use their objective best judgment and common sense when making this determination. Adherence to conda specifications is a particularly important aspect of the decision to include a project in the main conda organization. The membership of the initial Project Team should be included in the vote information. There is not requirement for a project to incubate before a vote of this nature can be called. This kind of vote applies only to software projects. Specifications are covered separately.

* Standard
* 60% Majority to pass

### Lock an Issue, Pull Request, Thread

Occasionally, discussions become toxic and antithetical to the goal of fostering the conda community. Steering Council members have the right to lock the thread in an "ask for forgiveness and not for permission" way so bad situations are handled quickly. The lock must be justified in the thread itself with a text explaining the reasons for locking and how the participants can contest it.

* Standard
* No need for voting to lock a thread

### Block a Contributor

In extreme cases, such as repeated harassment, it may become necessary to block a user completely from participating in all conda organization activities. This should not be done lightly, but it may be necessary to do so expediently. Shorter voting periods (at minimum 24 hrs) are allowed here. The proposer of the block must provide ample justification as to why this is needed.

* Sensitive
* 60% Majority to pass

### Remove a Steering Council member

The proposer must provide an overwhelming justification as to why the Steering Council member should be removed.

* Sensitive
* 75% Majority to pass

### Spending of funds

Proposers must specify the purpose, time limit, and source of funds that are to be spent. Purpose and time limit should be general enough in order to prevent excessive voting. For example, recurrent items (such as CI) should not need to be voted on each and every month. Instead, they should exist for a defined period of time (e.g. until the current migration ends, or for the next year). For such recurring expenses, the person coordinating spending the funds can choose to cancel the spending if it is deemed no longer necessary or cost-effective without calling another vote, although they should make reasonable efforts to notify the rest of the Steering Council before doing so.

Prior to their submission, grant proposals must be supplied to the Steering Council and a vote called under the `Spending of funds` policy. If the vote does not pass the proposal is not to be submitted in its current form and an additional round of voting is required on any subsequent draft. If the vote passes and the funds are awarded, further voting to spend the funds is not required.

* Standard
* Voting:
  * At least 50% participation
  * More than 50% "yes" votes to pass

### Modifying the governance document

The voting should happen in the PR in question and there must be a call to `@conda/steering`. The voting period must be open for at least one Steering Council meeting cycle to allow for clarification questions and discussions.

* Standard
* 75% Majority to pass

### Project Team Membership Appeal

An applicant to a Project Team that has been rejected from the team via the [Nominate new member of a Community Project Team](#nominate-new-member-of-a-community-project) policy below may appeal that decision to full Steering Council. Per the [Nominate new member of a Community Project Team](#nominate-new-member-of-a-community-project) policy
below, the proposer must provide a sufficient justification as to why the nominee should be welcomed into the Project Team. Prior
work on the project is an essential part of the nomination process. If the vote passes, the nominee is added to the Project Team.

* Sensitive
* Voting:
  * At least 50% participation
  * More than 50% "yes" votes to pass

### All Other Items

All other voting items, including Steering Council member funding sources, are considered to be standard and require a 50% majority to pass.

* Standard
* Voting:
  * At least 50% participation
  * More than 50% "yes" votes to pass

### Community Project Team Voting

Here are the minimal voting policies for Community Project Teams.

#### Nominate new member of a Community Project Team

The proposer must provide a sufficient justification as to why the nominee should be welcomed into the Project Team. Prior work on the project is an essential part of the nomination process. The voting body for these votes are the current members of the Project Team at the time the nomination is made.

* Sensitive
* Voting: One of the following:
  * at least 3 members voting, with all votes being "yes"
  * at least 50% participation, with greater than 50% "yes" votes to pass

#### Remove a Project Team Member

Sufficient justification must be given as to why a Project Team member should be removed. Removing a Project Team member who was added by the Steering Council via the [Project Team Membership Appeal](#project-team-membership-appeal) process may be considered a violation of the Code of Conduct if sufficient justification is not given.

* Sensitive
* Voting:
  * At least 50% participation
  * More than 50% "yes" votes to pass


## Current Steering Council Members

In alphabetical order,

{{ steering_members }}


## Emeritus Steering members

In alphabetical order,

{{ emeritus_members }}


## Document History

This document was initially written by [Anthony Scopatz](https://github.com/scopatz), [CJ Wright](https://github.com/CJ-Wright), [Matthew R. Becker](https://github.com/beckermr), [Uwe Korn](https://github.com/xhochy), and [Eric Dill](https://github.com/ericdill).  

In early 2022 several clarifications were made to this document. None of those clarifications change policies.

In mid 2022 provisional members and restrictions on shared funding of Steering Council members was added.

This document is released under the CC-BY 4.0 license.
