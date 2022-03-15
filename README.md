# Conda & Conda-Incubator Governance

This document outlines the policies and procedures that manage the conda community. This document recognizes that, while packaging and package tooling is deeply important to all of us, participation in the organization is voluntary. Individual members of the core team, any sub-team, and external contributors choose to participate and may choose to leave at any time for any reason or for no reason. 

Larger organizations, such as for-profit businesses, that contribute code and support to the conda organization are welcome to (but not required to) maintain creative control of their contributions as long as such contributions adhere to the rules in this document. Such organizations are also welcome to cede creative & maintenance control of any specific project to the community as well.

We deeply appreciate all good faith contributions.


## Code of Conduct

The conda organization's [Code of Conduct](CODE_OF_CONDUCT.md) governs all interactions within the conda organization.  Please take a few minutes to familiarize yourself with it.

Our code of conduct is based on the [NumFOCUS Code of Conduct template](https://github.com/numfocus/numfocus/blob/8759e21481552f213489e3718979ccecf68e9ead/manual/numfocus-coc.md).


## Naming & Manifest

This document defines the conda organization as the body responsible for governing the tools, specifications, and libraries within the conda ecosystem, broadly speaking. This encompasses specific GitHub organizations, such as [`conda`](https://github.com/conda/) and [`conda-incubator`](https://github.com/conda-incubator/). Authors of particular software projects, such as [`conda`](https://github.com/conda/conda) or [`mamba`](https://github.com/mamba-org/mamba), are free to choose if and when their projects are included as part of the conda organization.

This organization does not hold as part of its role the creation of any packages. The act of packaging itself has other organizations dedicated to their creation, such as [Anaconda](https://anaconda.com/), [conda-forge](https://conda-forge.org/), and [bioconda](https://bioconda.github.io/).


## Terminology

1. *conda* or *the conda organization* : The conda organization defined here, including `conda` and `conda-incubator`.
2. *The conda project* : The actual conda software itself, as distinct from the conda organization.
3. *The conda ecosystem* : The broadest set of tools, packages, and people that use any conda related tooling. The conda organization is a subset of *the conda ecosystem*. Members of the ecosystem should not feel compelled or obligated to participate in the conda organization, though positive engagement is welcome.


## Teams & Roles

The primary teams participating in the conda organization's activities are:

* **core:** The core team is the governing body over the entire conda organization. Members of the core team have full voting rights within the organization. Members of core are the face of the organization, and are responsible for officially interfacing with external communities, organizations, non-profits, and companies. The core team may create new sub-teams, as appropriate. Each member of core is entitled to one vote on all elected matters.
* **maintainers:** A maintainer is an individual or group responsible for the management of a software project consisting of one or more repositories and any software releases. Maintainers have the ability to merge pull requests into the repositories of the software project they maintain and produce releases of that software project.
* **external contributors:** This group encompasses all others who are not on core or maintainers. This includes first-time contributors, collaborators, and original authors. They have no special rights within the conda organization itself.
* **emeritus-core:** Core members that are inactive (commits, GitHub comments/issues/reviews, dev meetings, and voting on polls) in the past six months will be asked if they want to become emeritus-core developers. One week after asking, if the inactive core member has not responded, they will be automatically moved to emeritus status. Any core member can also request to become emeritus if they wish to do so (e.g. taking a sabbatical or long vacation). Emeritus core members can still vote and be brought back to active core anytime, but emeritus-core votes will not count towards the total core members when computing the necessary votes a poll needs to meet quorum. The [`core.csv`](core.csv) list should be updated when change in the status of a member occurs.


## Sub-Teams

The core team may elect to create new sub-teams for managing the daily business of the organization. While sub-teams may have non-core members, every sub-team must have at least one core team member at all times. If a sub-team fails to have a core team member for more than 1 week, that team is considered to be dissolved. A new sub-team would need to be established by the core in order to reinstate the activity.

Sub-teams have a charter that is either *dynamic* or *static*.

* A **dynamic** charter means that the sub-team is self-organizing, with respect to its own internal policies, procedures, and membership. A sub-team may choose to modify its membership independent of the core team. For example, a Google Summer of Code team could be a good candidate for a dynamic charter. Maintenance teams also have a dynamic charter, except for voting on commit rights and membership, as detailed below.
* A **static** charter means that all membership decisions and non-trivial policies changes must be approved by the core team. For example, a finance team may require a static charter.

All sub-teams must adhere to the governance, policies, and procedures of the conda organization at all times.


## Community, Federated, & Attic Maintenance

The conda organization acknowledges that project contributions may come from a variety of sources. To this end we define three maintenance categories for our projects.

* A **Community** maintained project is one where the development, ownership, and maintenance are controlled by the conda organization at large. Contributors keep the copyright for code they wrote and submit for inclusion to the respective project under the terms of license of that project. 
* A **Federated** project is maintained by a sub-team of *the conda organization*. Such projects maintain control of distribution and licensing via the project's sub-team. Federated projects are not controlled by the community at large. Still, as part of the conda organization, federated projects agree to the terms of this governance document, including but not limited to the [Code of Conduct](CODE_OF_CONDUCT.md).
* An **Attic** project is one which is unmaintained or clearly superseded by another project. No support is provided or anticipated for these projects. 

All projects must prominently list their maintenance status in their README and provide clear instructions on where people can seek help for the project. The possible maintenance statuses are one of `federated` or `community` or `attic`. 

All conda projects must use an [OSI approved software license](https://opensource.org/). We recommend and encourage the use of [BSD-family licenses](https://opensource.org/licenses/BSD-3-Clause). We recommend that specifications and documentation use [Creative Commons licenses](https://creativecommons.org/).

Project maintenance teams (defined below) decide among themselves whether or not to move their projects in and out of `attic` status. Core must be notified before this change and will mark `attic` projects as archived.


### The Rationale for Federated Projects

Federated projects enable conda ecosystem projects to exist under the same umbrella organization, while maintaining community standards. They acknowledge the time and investment the developers and authors have put into their creations and that in certain cases they wish to maintain creative control. A federated system also allows for a phased transition plan for projects to become increasingly community maintained over time.

Federated projects cannot expect that the community will maintain or support the project as long as the project remains federated. If/when a federated project transitions to the community maintenance model, this project will be maintained and supported by the community.

Federated projects are under no obligation to have a transition plan or any intention of becoming a community maintained project. However, this is strongly encouraged and community maintained projects are seen as the ideal. Federated projects are seen as the reality.


## Incubation

All projects start their journeys in an experimental or unstable state. To this end, we delineate stable projects as living in the `conda` GitHub organization. Therefore, projects new to the conda organization and governance must begin their inclusion here in the `conda-incubator` organization. The barrier to entry for a project to be added to the incubator should be very low. A vote from core is required to move a project from incubation to the main GitHub organization.

Any single member of core may add a project to the incubator, given the knowledge and consent of the author (see [below](#voting)). The member of core sponsoring the incubation is responsible for ensuring that basic legal requirements have been met that allow for the incubation. For example, trademark usage and license terms must been checked prior to incubation.


## Maintenance Teams

A maintenance team is a sub-team with a dynamic charter, except for a few caveats as detailed here. They exist to maintain a specific project (or possibly set of projects). Each project in `conda` or `conda-incubator` should belong to exactly one maintenance team. This team is granted write access to the repos associated with the project.

The initial maintenance team for projects in the `conda` organization are specified in the vote to move a project from the incubator to the main `conda` organization. As this vote has a 60% threshold and sub-team formation is only a greater than 50% threshold, the vote for adding a project to the main `conda` organization can serve both purposes. Maintenance teams for incubating projects do not need a vote for their creation. Instead they are created when the project is moved into `conda-incubator`.

For federated and incubating projects, the maintenance team decides among themselves on how to add and/or remove members from the maintenance team. Further, maintenance teams for incubating projects are exempted from the requirement to have at least one core member. For a community maintained project, a petition for commit rights is made to the current members of the maintenance team for that project. If this petition passes according to the voting rules for "Nominate new member of a maintenance team" below, the petitioner is granted write access and added to the team.

Members of **core** are excluded from these votes and retain commit rights to all community projects as stated above. They can add or remove themselves from maintenance teams as they see fit in order to indicate which projects they are involved with, have a say in voting for write access petitions, etc. Members of core may not add themselves to a maintenance team in order to vote on a petition for commit access if they were not already on that team when the petition was made. 


## Voting

This section presents descriptions and criteria for voting items in the conda organization. The core team is the only team with voting rights. Members of core may also call a vote on any topic. The restrictions on calling a vote are as follows:

* There must only be one vote active on a particular item at any time.
* The act of calling for a vote must not itself violate the code of conduct. For example, Sam repeatedly called for votes immediately after a previous vote failed to achieve Sam's result. Sam is attempting to bully other members of core into agreeing, and is thus violating the code of conduct.
* Voting yes moves the proposal forward; 
  Voting no is the only way to express opposition to the proposal;
  There is always an option to abstain from voting;
  Not voting is discouraged, but non-votes do not count as "no", "yes", or "abstain".
* Core members must explicitly abstain from a vote via making a comment on the PR/issue or selecting the "abstain" option. Simply not voting at all doesn't count as an abstention.
* Abstentions count towards the quorum but are excluded when computing if a vote passes. 

Voting items are labeled as either **standard** or **sensitive**. Standard items are ones where public record and discourse is preferable. Sensitive voting items are ones where the results of the vote should remain private to the voters after the vote has occurred. Sensitive votes should take place on a secure anonymous voting platform in order to retain election integrity and anonymity. (We may use [`Polys`](https://polys.me) and the [`Helios voting system`](https://vote.heliosvoting.org/), but are open to any secure, anonymous system.) The email capability of your chosen voting platform should be used for sending voting invitations and reminders, and you should use the email list from `core.csv` as the authoritative list of emails to use.

The default voting period is 1 week (7 days). This may be modified at the time when a vote is called, but may never be less than one week modulo exceptions for some time-sensitive votes below.

Additional requirements may apply in case low turnouts have to be handled, see "Quorum" below.

To call for a standard vote, here is a template Issue/PR comment:

    @conda/core
    This PR falls under the {policy} policy, please vote and/or comment on this PR.
    This PR needs {policy_percent} of core to vote yea to pass.
    To vote please leave Approve (yea) or Request Changes (nay) reviews.
    If you would like changes to the current language please leave a comment or push to this branch.
    This vote will end on {date}.

A `vote` label must be applied to the PR or issue.

----

**Posting results:** To maintain the historical record, the outcome of any standard vote which invoked the timeout rules below should be recorded in the `vote-results` folder of our documentation. 

Each "timed out" vote should be its own file.  The filename should reflect the topic and the date that the vote opened. The file should contain at least:
         
* vote description
* vote policy
* vote totals
* Poll open and close dates
* documentation of the vote reminders as detailed below

Non-timed-out vote results should be documented in github PR/issue upon which the voting happened. A `vote` label must be applied to the PR or issue.

----

**Quorum:** With one exception, all percentages below express *both* required participation, as a fraction of the active core team, as well as the fraction of that fraction who vote affirmatively (i.e. vote `yes`) on the issue. The exception is when 50% is required.  In these cases, *at least half* of team members need to participate, but *more than 50%* of votes need to be affirmative for the vote to pass.

For example, in a vote requiring 50% participation, with 20 active members, at least 10 must vote; if 10 or 11 vote, there must be at least 6 affirmative votes. If 12 or 13 members vote, at least 7 votes must be affirmative to pass, and so on.

Because everyone is busy and it is difficult sometimes to get quorum, votes not achieving quorum will eventually time out on their set end date. When this happens, the current participation level is taken for what it is, and the percentage of affirmative votes is calculated from whatever the vote total is at that time. In order for a timeout to occur, the vote must have:

* been open for at least 2 weeks
* been presented and discussed at a Core team meeting
* been advertised on at least 3 separate occasions on the core chat channel (beginning of voting period, middle, and one day prior to proposed timeout) 
* been sent to core members via email. Email reminders must have been sent similarly to the core chat channel: at least 3 times, occurring as beginning of voting period, middle, and one day prior to proposed timeout.

Extending the above example, if 9 people are required for a quorum, but only 7 have voted, those 7 votes can form the basis of a completed vote after the above conditions are met. 4 votes within those 7 would be needed to pass the vote.

To post a timeout reminder, here is a template comment:

    @conda/core
    This vote falls under the {policy} policy, please vote and/or comment on this PR.
    This vote needs {policy_percent} of core to vote yea to pass.
    This vote presently has {current_voters}, and needs {policy_percent * core - current_voters} more for quorum.
    It is proposed that this vote will time out and be evaluated with the current votes in {days}, on {date}.
    To vote please leave Approve (yea) or Request Changes (nay) reviews.
              
To declare a standard vote "timed out," the person making such a declaration must post a pull-request adding a vote record to the `vote-results` folder. The declaration PR should be merged by the first core member who is available to verify that the requirements for the timeout have been met, based on their own personal records.

----

**Voting Total Examples**

Assume the core team has 10 active members, 2 emeritus members, and the vote threshold is 50%.

1. Among core there are 3 "yes", 2 "no", and 1 "abstain" votes. No emeritus votes were recorded. This vote has reached quorum (3 + 2 + 1 = 6 which is at least 50% of 10). It also passes since it recorded 3 "yes" votes and 2 "no" votes giving 3/5 (60%) which is greater than 50% of 5.

2. Among core there are 4 "yes", 2 "no", and no abstentions. One emeritus core member voted "no". This vote has reached quorum (4 + 2 = 6 which is at least 50% of 10). It has also passed since it recorded 4 "yes" votes and 3 "no" votes giving 4/7 which is greater than 50% of 6.

3. Among core there are 3 "yes" votes, "1" no vote and no abstentions. No emeritus members voted. Further the timeout rules above **were** invoked. This vote has thus reached quorum and it has passed since 3/4 (75%) is greater than 50%.

4. Among core there are 3 "yes" votes, "1" no vote and no abstentions. No emeritus members voted. Further the timeout rules above **were not** invoked. This vote has not reached quorum and should be extended or redone.

----

**Enhancement Proposal Approval:** When ready, the proposer may call for a vote on an existing conda enhancement proposal (CEP). This requires a super-majority (60%) to pass so that the decision to accept the CEP is unequivocal and we have ensured that consensus has been reached.

* Standard
* 60% Majority to pass

----

**Nominate new member of core:** The proposer must provide a sufficient justification as to why the nominee should be welcomed into core. Prior service to the community, including but not limited to: working on conda organization projects, writing conda specifications, and helping to bridge disparate communities are an important part of the nomination process.

* Sensitive
* 2/3rds Majority to pass

----

**Nominate new member of a maintenance team:** The proposer must provide a sufficient justification as to why the nominee should be welcomed into the maintenance team. Prior work on the project is an essential part of the nomination process. The voting body for these votes are the current members of the maintenance team at the time the nomination is made.

* Sensitive
* Voting: One of the following:
  * at least 3 members voting, with all votes being "yes"
  * at least 50% participation, with greater than 50% "yes" votes to pass

----

**Sub-team Formation:** Proposers must specify the name, role & responsibility, members, and charter (dynamic or static) of any new sub-teams.

* Standard
* Voting:
  * At least 50% participation
  * More than 50% "yes" votes to pass

----

**Sub-team Dissolution:** Proposers must specify the name and justification for why a sub-team should be dissolved.

* Standard
* Voting:
  * At least 50% participation
  * More than 50% "yes" votes to pass

----

**Add Project/Repo to Incubator:** Any single member of core may add a project to the incubator, given the knowledge and consent of the author(s). The low barrier to entry here is because we want to encourage innovation, experimentation, and growth.  Members of core are encouraged to use common sense when adding new projects to the `conda-incubator` organization.

* Standard
* 1 member of core willing to add the repository, no vote required

----

**Remove Project/Repo from Incubator:** While we do not anticipate this ever being necessary, if the situation arises where a project needs to be removed from the incubator, two potential options are available, depending on the copyright and maintenance of the project. 

In the first, easy case, the incubated project has been wholly developed and maintained by the authors. Here, the project should be allowed to leave incubation if the developers of that project decide and consent to leave. No vote from core is required. A willing core member may be needed to transfer the repository, though.

In the second case, the incubated project has been communally developed by other members of the conda organization AND/OR the copyright of the project has been transferred to the conda organization, NumFOCUS, or a similar entity that is larger than the developers/copyright holders at the time of initial incubation.  In this case, core must decide whether or not to allow the project to leave. A simple vote is required.

* Standard
* Voting:
  * At least 50% participation
  * More than 50% "yes" votes to pass

----

**Incorporate a Software Project into the main `conda` Organization:** At some point, many projects will want to be included in the main `conda` GitHub (or otherwise) organization. Moving a project into this organization can be done with a super-majority vote from core. There are no strict criteria for when a project is ready, stable, or viable for this step. Rather, members of core are entrusted to use their objective best judgment and common sense when making this determination. Adherence to conda specifications is a particularly important aspect of the decision to include a project in the main conda organization. The membership of the initial maintenance team should be included in the vote information. There is not requirement for a project to incubate before a vote of this nature can be called. This kind of vote applies only to software projects. Specifications are covered separately.

* Standard
* 60% Majority to pass

----

**Graduate a Specification Project from Incubation to Main:** The purpose of specifications is to be fully endorsed by the main conda organization. Graduating a specification can be done with a super-super-majority vote from core. The purpose of this is to ensure that the overwhelming majority of the conda ecosystem agrees with the goals & aims of the specification, even if no software implements it at the time of the vote. Specifications are highly encouraged to be written and developed in `conda-incubator` so they can accrue comments and changes. New versions of a specification (beyond simple typographical and grammatical fixes) are considered new specifications for purposes of voting here. 

In spite of the high threshold for approval here, we highly encourage the writing of specification documents. 

* Standard
* 70% Majority to pass

----

**Lock an Issue, Pull Request, Thread:** Occasionally, discussions become toxic and antithetical to the goal of fostering the conda community. Members of core have the right to lock the thread in an "ask for forgiveness and not for permission" way so bad situations are handled quickly. The lock must be justified in the thread itself with a text explaining the reasons for locking and how the participants can contest it.

* Standard
* No need for voting to lock a thread

----

**Block a Contributor:** In extreme cases, such as repeated harassment, it may become necessary to block a user completely from participating in all conda organization activities. This should not be done lightly, but it may be necessary to do so expediently. Shorter voting periods (at minimum 24 hrs) are allowed here. The proposer of the block must provide ample justification as to why this is needed.

* Sensitive
* 60% Majority to pass

----

**Remove member of core:** The proposer must provide an overwhelming justification as to why the member core should be removed.

* Sensitive
* 75% Majority to pass

----

**Spending of funds:** Proposers must specify the purpose, time limit, and source of funds that are to be spent. Purpose and time limit should be general enough in order to prevent excessive voting. For example, recurrent items (such as CI) should not need to be voted on each and every month. Instead, they should exist for a defined period of time (e.g. until the current migration ends, or for the next year). For such recurring expenses, the person coordinating spending the funds can choose to cancel the spending if it is deemed no longer necessary or cost-effective without calling another vote, although they should make reasonable efforts to notify the rest of core before doing so.

Prior to their submission, grant proposals must be supplied to the core members and a vote called under the `Spending of funds` policy. If the vote does not pass the proposal is not to be submitted in its current form and an additional round of voting is required on any subsequent draft. If the vote passes and the funds are awarded, further voting to spend the funds is not required.

* Standard
* Voting:
  * At least 50% participation
  * More than 50% "yes" votes to pass

----

**Modifying the governance document:** The voting should happen in the PR in question and there must be a call to `@conda/core`. The voting period must be open for at least one core member meeting cycle to allow for clarification questions and discussions.

* Standard
* 75% Majority to pass

----

All other voting items are considered to be standard and require a 50% majority to pass.


## Ratification of this Document

In order initiate the conda organization described here, anyone is able to participate and become a member of the starting core team (or emeritus team). In order to be founding core team member, an individual must perform the following actions:

1. Each individual has to participate in the vote to ratify this governance document,
2. Each individual has to personally add their own name - and only their own name - to the core.csv or emeritus.csv file.

These criteria are intended to be inclusive while having founding core members demonstrate a real interest in participating. 

Interested individuals should use their own judgment and discretion when determining if they should be a founding core member. Being a founding core member implies the intention to participate in this organization through voting, governance discussions, core meetings, etc.  If you are not in a current position to have this level of engagement but anticipate this level of engagement at a future date, consider signing on with initial emeritus status.

There is no obligation or need to become a core member, if this is not relevant to you. This organization will be making a number of sub-teams, which we welcome and invite the broader conda ecosystem to participate in, when it is of interest.

We encourage everyone to find their niche in this organization, and welcome participation at any and all levels.

The vote for ratification of this governance document is public and requires a 75% majority of those participating in the vote to pass.

**Timeline:**

1. A draft version of this document will be proposed for general review and comment (RFC). This RFC period must last at least 7 days before a vote can be called.
2. A vote on the reviewed document is called and will be open for exactly 7 days. 
   * If the vote fails, return to step 1.
   * If the vote passes, continue to step 2.
3. Individuals who participated in the vote are able to add themselves to the core.csv or emeritus.csv file. After doing so, they are considered members of the core team.

If for some reason someone is unable to make the timeline when the vote is called, that person can always be added to the core team later via the normal process. 


## Current Members of Core

In alphabetical order,

{{ core_members }}


## Emeritus members

In alphabetical order,

{{ emeritus_members }}


## Document History

This document was initially written by Anthony Scopatz, CJ Wright, Matthew R. Becker, Uwe Korn, and Eric Dill.

This document is released under the CC-BY 4.0 license.