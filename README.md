# Conda & Conda-Incubator Governance

This repository contains the policies and procedures that manage the conda community. These documents recognize that, while packaging and package tooling is deeply important to all of us, participation in the organization is voluntary. Individual members of the [Steering Council](governance.md/#steering-council), any [sub-team](governance.md/#sub-teams), and external contributors choose to participate and may choose to leave at any time for any reason or for no reason.

Larger organizations, such as for-profit businesses, that contribute code and support to the conda organization are welcome to (but not required to) [maintain creative control](governance.md/#federated-projects) of their contributions as long as such contributions adhere to the rules in this document. Such organizations are also welcome to [cede creative & maintenance control](governance.md/#community-projects) of any specific project to the community as well.

We deeply appreciate all good faith contributions.

## Quick Links

- [Request for Incubation](https://github.com/conda/governance/issues/new?template=incubation_request.yml)
- [Request for Graduation](https://github.com/conda/governance/issues/new?template=graduation_request.yml)
- [New Sub-team/Project Team](https://github.com/conda/governance/issues/new?template=new_team.yml)

## Code of Conduct

The conda Organization's [Code of Conduct](CODE_OF_CONDUCT.md) governs all interactions within the conda Organization. Please take a few minutes to familiarize yourself with it.

## Governance

The primary groups participating in the conda Organization's activities are:

- [**Steering Council:**](steering-council/charter.md) governing body over the conda Organization.
  Steering Council members are the face of the organization, and are responsible for officially interfacing with external communities, organizations, non-profits, and companies. The Steering Council is the only group with voting rights at the conda Organization level (see [Voting](steering-council/charter.md/#voting) for more details).
- **Sub-Teams:** persistent open groups that manage the day-to-day business of the organization. All sub-teams must adhere to the governance, policies, and procedures of the conda Organization at all times. Sub-teams have either a _dynamic_ or _static_ charter.
- **Project Teams:** are responsible for the management of a software project.
- **Emeritus Steering:** inactive members that stepped down from their Steering Council duties.
- **External Contributors:** individuals that are not part of the Steering Council, sub-teams or project teams but contribute to the conda organization.

See the [full conda governance documentation](governance.md) for more details on these groups.



## Voting items

### Enhancement Proposal Approval

When ready, the proposer may call for a vote on an existing [conda enhancement proposal (CEP)](https://github.com/conda/ceps). This requires a super-majority (60%) to pass so that the decision to accept the CEP is unequivocal and we have ensured that consensus has been reached.

- Standard
- 60% Majority to pass

### Nominate new Steering Council member

The proposer must provide a sufficient justification as to why the nominee should be welcomed into the Steering Council. Prior service to the community, including but not limited to: working on conda organization projects, writing conda specifications, and helping to bridge disparate communities are an important part of the nomination process.

- Sensitive
- 2/3rds Majority to pass

### Nominate a Provisional Steering Council Member

The proposer must provide a sufficient justification as to why the nominee should be welcomed on a provisional basis into the Steering Council. The guidelines on [Provisional Members](#provisional-members) must be followed as well.

- Sensitive
- Voting:
  - At least 50% participation
  - More than 50% "yes" votes to pass

### Remove a Provisional Steering Council Member

The proposer must provide a sufficient justification as to why the provisional member should be removed. The guidelines on [Provisional Members](#provisional-members) must be followed as well.

- Sensitive
- Voting:
  - At least 50% participation
  - More than 50% "yes" votes to pass

### Resolve Overlapping Funding

In the case that more than two Steering Council members [share the same funding source](#shared-funding-membership-restrictions) and no agreement can be reached
among the members with shared funding as to who will enter [emeritus status](#emeritus-steering), the Steering Council will hold a simple
plurality vote in order to resolve the funding conflict. Each member with shared funding will be listed as a separate option in the
vote. The Steering Council will then vote on which member should be moved to emeritus status. The member who receives the most votes is moved to emeritus status. The quorum for this vote is five. In the case of a tie, the member is chosen at random.

- Sensitive
- Voting:
  - Simple plurality of votes
  - Member with most votes is moved to emeritus status
  - Ties are resolved by choosing a member at random
  - The quorum for this vote is five votes

### Sub-team Formation

Proposers must specify the name, role & responsibility, members, and charter (dynamic or static) of any new [sub-teams](#sub-teams).

- Standard
- Voting:
  - At least 50% participation
  - More than 50% "yes" votes to pass

### Sub-team Dissolution

Proposers must specify the name and justification for why a sub-team should be dissolved.

- Standard
- Voting:
  - At least 50% participation
  - More than 50% "yes" votes to pass

### Add Project/Repo to Incubator

Any single Steering Council member may add a project to the [incubator](#incubation), given the knowledge and consent of the author(s). The low barrier to entry here is because we want to encourage innovation, experimentation, and growth. Steering Council members are encouraged to use common sense when adding new projects to the `conda-incubator` organization.

- Standard
- 1 Steering Council member willing to add the repository, no vote required

### Remove Project/Repo from Incubator

While we do not anticipate this ever being necessary, if the situation arises where a project needs to be removed from the [incubator](#incubation), two potential options are available, depending on the copyright and maintenance of the project.

In the first, easy case, the incubated project has been wholly developed and maintained by the authors. Here, the project should be allowed to leave incubation if the developers of that project decide and consent to leave. No vote from the Steering Council is required. A willing Steering Council member may be needed to transfer the repository, though.

In the second case, the incubated project has been communally developed by other members of the conda organization AND/OR the copyright of the project has been transferred to the conda organization, NumFOCUS, or a similar entity that is larger than the developers/copyright holders at the time of initial incubation. In this case, the Steering Council must decide whether or not to allow the project to leave. A simple vote is required.

- Standard
- Voting:
  - At least 50% participation
  - More than 50% "yes" votes to pass

### Incorporate a Software Project into the main `conda` Organization

At some point, many projects will want to be included in the main `conda` GitHub (or otherwise) organization. Moving a project into this organization can be done with a super-majority vote from the Steering Council. There are no strict criteria for when a project is ready, stable, or viable for this step. Rather, Steering Council members are entrusted to use their objective best judgment and common sense when making this determination. Adherence to conda specifications is a particularly important aspect of the decision to include a project in the main conda organization. The membership of the initial [Project Team](#project-teams) should be included in the vote information. There is not requirement for a project to incubate before a vote of this nature can be called. This kind of vote applies only to software projects.

- Standard
- 60% Majority to pass

### Lock an Issue, Pull Request, Thread

Occasionally, discussions become toxic and antithetical to the goal of fostering the conda community. Steering Council members have the right to lock the thread in an "ask for forgiveness and not for permission" way so bad situations are handled quickly. The lock must be justified in the thread itself with a text explaining the reasons for locking and how the participants can contest it.

- Standard
- No need for voting to lock a thread

### Block a Contributor

In extreme cases, such as repeated harassment, it may become necessary to block a user completely from participating in all conda organization activities. This should not be done lightly, but it may be necessary to do so expediently. Shorter voting periods (at minimum 24 hrs) are allowed here. The proposer of the block must provide ample justification as to why this is needed.

- Sensitive
- 60% Majority to pass

### Remove a Steering Council member

The proposer must provide an overwhelming justification as to why the Steering Council member should be removed.

- Sensitive
- 75% Majority to pass

### Spending of funds

Proposers must specify the purpose, time limit, and source of funds that are to be spent. Purpose and time limit should be general enough in order to prevent excessive voting. For example, recurrent items (such as CI) should not need to be voted on each and every month. Instead, they should exist for a defined period of time (e.g. until the current migration ends, or for the next year). For such recurring expenses, the person coordinating spending the funds can choose to cancel the spending if it is deemed no longer necessary or cost-effective without calling another vote, although they should make reasonable efforts to notify the rest of the Steering Council before doing so.

Prior to their submission, grant proposals must be supplied to the Steering Council and a vote called under the `Spending of funds` policy. If the vote does not pass the proposal is not to be submitted in its current form and an additional round of voting is required on any subsequent draft. If the vote passes and the funds are awarded, further voting to spend the funds is not required.

- Standard
- Voting:
  - At least 50% participation
  - More than 50% "yes" votes to pass

### Modifying the governance document

The voting should happen in the PR in question and there must be a call to `@conda/steering`. The voting period must be open for at least one Steering Council meeting cycle to allow for clarification questions and discussions.

- Standard
- 75% Majority to pass

### Project Team Membership Appeal

An applicant to a Project Team that has been rejected from the team via the [Nominate new member of a Community Project Team](#nominate-new-member-of-a-community-project) policy below may appeal that decision to full Steering Council. Per the [Nominate new member of a Community Project Team](#nominate-new-member-of-a-community-project) policy
below, the proposer must provide a sufficient justification as to why the nominee should be welcomed into the Project Team. Prior
work on the project is an essential part of the nomination process. If the vote passes, the nominee is added to the Project Team.

- Sensitive
- Voting:
  - At least 50% participation
  - More than 50% "yes" votes to pass

### All Other Items

All other voting items, including Steering Council member funding sources, are considered to be standard and require a 50% majority to pass.

- Standard
- Voting:
  - At least 50% participation
  - More than 50% "yes" votes to pass

### Community Project Team Voting

Here are the minimal voting policies for [Community Project](#community-projects) Teams.

#### Nominate new member of a Community Project Team

The proposer must provide a sufficient justification as to why the nominee should be welcomed into the Project Team. Prior work on the project is an essential part of the nomination process. The voting body for these votes are the current members of the [Project Team](#project-teams) at the time the nomination is made.

- Sensitive
- Voting: One of the following:
  - at least 3 members voting, with all votes being "yes"
  - at least 50% participation, with greater than 50% "yes" votes to pass

#### Remove a Project Team Member

Sufficient justification must be given as to why a Project Team member should be removed. Removing a Project Team member who was added by the Steering Council via the [Project Team Membership Appeal](#project-team-membership-appeal) process may be considered a violation of the Code of Conduct if sufficient justification is not given.

- Sensitive
- Voting:
  - At least 50% participation
  - More than 50% "yes" votes to pass

## Current Steering Council Members

In alphabetical order,

<!-- STEERING-TABLE -->
| Name | GitHub | Funder | Pronouns |
| --- | --- | --- | --- |
| Bas Zalmstra | [@baszalmstra](https://github.com/baszalmstra) | prefix.dev | he/him |
| Cheng H. Lee | [@chenghlee](https://github.com/chenghlee) | Anaconda | he/him |
| Hind Montassif | [@Hind-M](https://github.com/Hind-M) | QuantStack | she/her |
| Jaime Rodríguez-Guerra | [@jaimergp](https://github.com/jaimergp) | Quansight | he/him |
| Jannis Leidel | [@jezdez](https://github.com/jezdez) | Anaconda | he/him |
| John Kirkham | [@jakirkham](https://github.com/jakirkham) | NVIDIA | he/him |
| Marcelo Duarte Trevisani | [@marcelotrevisani](https://github.com/marcelotrevisani) | no funding | he/him |
| Marius van Niekerk | [@mariusvniekerk](https://github.com/mariusvniekerk) |  |  |
| Michael Sarahan | [@msarahan](https://github.com/msarahan) | NVIDIA | he/him |
| Pavel Zwerschke | [@pavelzw](https://github.com/pavelzw) | QuantCo | he/him |
| Tania Allard | [@trallard](https://github.com/trallard) | Quansight | she/her |
| Uwe Korn | [@xhochy](https://github.com/xhochy) | QuantCo | he/him |
| Wolf Vollprecht | [@wolfv](https://github.com/wolfv) | prefix.dev | he/him |
<!-- END-OF-STEERING-TABLE -->

## Emeritus Steering members

In alphabetical order,

<!-- EMERITUS-TABLE -->
| Name | GitHub | Funder | Pronouns |
| --- | --- | --- | --- |
| Angela Gloyna | [@angloyna](https://github.com/angloyna) |  |  |
| Anthony Scopatz | [@scopatz](https://github.com/scopatz) |  |  |
| Christopher J. 'CJ' Wright | [@cj-wright](https://github.com/cj-wright) |  |  |
| Connor Martin | [@cjmartian](https://github.com/cjmartian) |  |  |
| Crystal Soja | [@csoja](https://github.com/csoja) |  |  |
| Dharhas Pothina | [@dharhas](https://github.com/dharhas) |  |  |
| Eric Dill | [@ericdill](https://github.com/ericdill) |  |  |
| Filipe Fernandes | [@ocefpaf](https://github.com/ocefpaf) | no funding | he/him |
| Gonzalo Peña-Castellanos | [@goanpeca](https://github.com/goanpeca) | Quansight | he/him |
| Jonathan Helmus | [@jjhelmus](https://github.com/jjhelmus) |  |  |
| Keith Kraus | [@kkraus14](https://github.com/kkraus14) | no funding | he/him |
| Marcel Bargull | [@mbargull](https://github.com/mbargull) |  |  |
| Martin Prüsse | [@prusse-martin](https://github.com/prusse-martin) |  |  |
| Matthew R. Becker | [@beckermr](https://github.com/beckermr) | no funding | he/him |
| Megan Yancy | [@myancy-anaconda](https://github.com/myancy-anaconda) |  |  |
| Michael Grant | [@mcg1969](https://github.com/mcg1969) |  |  |
| Min Ragan-Kelley | [@minrk](https://github.com/minrk) |  |  |
| Patrick Sodré | [@sodre](https://github.com/sodre) |  |  |
| Ray Douglass | [@raydouglass](https://github.com/raydouglass) |  |  |
| Sebastien Awwad | [@awwad](https://github.com/awwad) |  |  |
| Travis Oliphant | [@teoliphant](https://github.com/teoliphant) |  |  |
<!-- END-OF-EMERITUS-TABLE -->

## Document History

This document was initially written by [Anthony Scopatz](https://github.com/scopatz), [CJ Wright](https://github.com/CJ-Wright), [Matthew R. Becker](https://github.com/beckermr), [Uwe Korn](https://github.com/xhochy), and [Eric Dill](https://github.com/ericdill).

In early and late 2022 several clarifications were made to this document. None of those clarifications change policies.

In mid 2022 provisional members and restrictions on shared funding of Steering Council members was added.

This document is released under the CC-BY 4.0 license.
