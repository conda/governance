# conda community governance

This is a Work in progress, documenting how we have been operating up to this point.

- [conda community governance](#conda-community-governance)
  - [Naming \& Manifest](#naming--manifest)
  - [Terminology](#terminology)
  - [Teams \& Roles Overview](#teams--roles-overview)
    - [Steering Council](#steering-council)
    - [Sub-Teams](#sub-teams)
      - [Dynamic Charter](#dynamic-charter)
      - [Static Charter](#static-charter)
    - [Project Teams](#project-teams)
    - [Emeritus Steering](#emeritus-steering)
    - [External Contributors](#external-contributors)
  - [Community, Federated \& Archive Maintenance (Projects)](#community-federated--archive-maintenance-projects)
    - [Community Projects](#community-projects)
    - [Federated Projects](#federated-projects)
    - [The Rationale for Federated Projects](#the-rationale-for-federated-projects)
    - [Archive Projects](#archive-projects)
    - [Project Requirements](#project-requirements)
  - [Trademarks](#trademarks)
  - [Incubation](#incubation)

## Naming & Manifest

This document defines the _conda Organization_ as the body responsible for governing the tools, specifications, and libraries within the conda ecosystem, broadly speaking. This encompasses specific GitHub organizations, such as [`conda`](https://github.com/conda/), [`conda-incubator`](https://github.com/conda-incubator/) and [`conda-archive`](https://github.com/conda-archive/). Authors of particular software projects, such as [`conda`](https://github.com/conda/conda) or [`mamba`](https://github.com/mamba-org/mamba), are free to choose when their projects are included as part of the conda Organization.

This organization does not hold as part of its role the creation of any packages. The act of packaging itself has other organizations dedicated to their creation, such as [conda-forge](https://conda-forge.org/), [Bioconda](https://bioconda.github.io/), and [Anaconda](https://anaconda.com/).

## Terminology

1. **conda** or the **conda Organization** : The conda Organization defined here, including `conda`, `conda-incubator` and `conda-archive`.
2. The **[conda project](https://github.com/conda/conda)** : The actual conda software itself, as distinct from the conda Organization.
3. The **conda ecosystem** : The broadest set of tools, packages, and people that use any conda related tooling. The conda Organization is a subset of _the conda ecosystem_. Members of the ecosystem should not feel compelled or obligated to participate in the conda Organization, though positive engagement is welcome.

## Teams & Roles Overview

The primary teams participating in the conda Organization's activities are:

### Steering Council

The [**Steering Council**](steering-council/charter.md) is the governing body over the entire conda Organization. Members of the Steering Council have full voting rights within the organization. Steering Council members are the face of the organization, and are responsible for officially interfacing with external communities, organizations, non-profits, and companies. The Steering Council may create new sub-teams, as appropriate. Each Steering Council member is entitled to one vote on all elected matters.

See the [Steering Council documentation](steering-council/charter.md) for more information about this team and its responsibilities.

### Sub-Teams

The Steering Council may elect to create new **sub-teams** for managing the daily business of the organization. While sub-teams may have non-Steering members, **every sub-team must have at least one [non-provisional](steering-council/charter.md#provisional-members) Steering Council team member at all times.** If a sub-team fails to have a Steering Council member for more than 1 week, that team is considered to be dissolved. A new sub-team would need to be established by the Steering Council in order to reinstate the activity.

All sub-teams must adhere to the governance, policies, and procedures of the conda Organization at all times. Sub-teams have either a _dynamic_ or _static_ charter.

#### Dynamic Charter

A **dynamic** charter means that the sub-team is self-organizing, with respect to any additional, internal policies, procedures, and membership. A sub-team may choose to modify its membership independent of the Steering Council. For example, a Google Summer of Code team could be a good candidate for a dynamic charter. Project Teams also have a dynamic charter.

#### Static Charter

A **static** charter means that all membership decisions and non-trivial policy changes must be approved by the Steering Council. For example, a finance team may require a static charter.

### Project Teams

**Project Teams** are responsible for the management of a software project consisting of one or more repositories and any software releases. Project Team members have the ability to merge pull requests into the repositories of the software project they maintain, produce releases of that software project, and all other duties related to repo maintenance. See the [Project Teams Details](project-team/charter.md) section for more.

### Emeritus Steering

[Steering Council](#steering-council) members that are inactive (commits, GitHub comments/issues/reviews, dev meetings, and voting on polls) in the past six months will be asked if they want to become **Emeritus Steering** members. One week after asking if the inactive Steering Council member has not responded, they will be automatically moved to emeritus status. Any Steering Council member can also request to become Emeritus if they wish to do so (e.g. taking a sabbatical or long vacation). Emeritus Steering members can be brought back to active Steering Council membership at anytime, assuming there is space and no other policies (e.g., [shared funding](steering-council/charter.md/#shared-funding-membership-restrictions), [council size](steering-council/charter.md/#steering-council-size), etc.) are violated. Emeritus Steering Council members cannot vote. When the status of a member changes, the corresponding `teams/` YAML files should be immediately updated to reflect the member's new position.

### External Contributors

This group encompasses all others who are not on the [Steering Council](#steering-council), [Sub-teams](#sub-teams), or [Project Teams](#project-teams). This includes first-time contributors, collaborators, and original authors. They have no special rights within the conda Organization itself.

## Community, Federated & Archive Maintenance (Projects)

The conda Organization acknowledges that project contributions may come from a variety of sources. To this end we define three maintenance categories for our projects.

### Community Projects

A **Community** maintained project is one where the development, ownership, and maintenance are controlled by the conda Organization at large. Contributors keep the copyright for code they wrote and submit for inclusion to the respective project under the terms of license of that project.

### Federated Projects

A **Federated** project is maintained by a sub-team of _the conda Organization_. Such projects maintain control of distribution and licensing via the project's sub-team. Federated projects are not controlled by the community at large. Still, as part of the conda Organization, federated projects agree to the terms of this governance document, including but not limited to the [Code of Conduct](CODE_OF_CONDUCT.md). See [The Rationale for Federated Projects](#the-rationale-for-federated-projects) section below for more.

### The Rationale for Federated Projects

[Federated projects](#federated-projects) enable conda ecosystem projects to exist under the same umbrella organization, while maintaining community standards. They acknowledge the time and investment the developers and authors have put into their creations and that in certain cases they wish to maintain creative control. A federated system also allows for a phased transition plan for projects to become increasingly community maintained over time.

Federated projects cannot expect that the community will maintain or support the project as long as the project remains federated. If/when a federated project transitions to the community maintenance model, this project will be maintained and supported by the community.

Federated projects are under no obligation to have a transition plan or any intention of becoming a community maintained project. However, this is strongly encouraged and community maintained projects are seen as the ideal. Federated projects are seen as the reality.

### Archive Projects

An **Archive** project is one which is unmaintained or clearly superseded by another project. No support is provided or anticipated for these projects.

### Project Requirements

All projects must prominently list their maintenance status in their README and provide clear instructions on where people can seek help for the project. The possible maintenance statuses are one of [`federated`](#federated-projects) or [`community`](#community-projects) or [`archive`](#archive-projects).

**All conda projects must use an [OSI approved software license](https://opensource.org/).** We recommend and encourage the use of [BSD-family licenses](https://opensource.org/licenses/BSD-3-Clause). We recommend that specifications and documentation use [Creative Commons licenses](https://creativecommons.org/).

[Project Teams](#project-teams) decide among themselves whether or not to move their projects in and out of `archive` status. The Steering Council must be notified before this change and will move `archive` projects to the `conda-archive` organization and mark them as archived.

## Trademarks

[Community Projects](#community-projects) need to license/assign the project's trademarks when becoming a conda Organization Community Project. This is an act of good faith and communicates to the community that the project is committed to our overall efforts.

1. Trademarks are irrevocably _licensed or transferred_ to the conda Organization's fiscal sponsor when a project is added to the conda Organization as a Community Project.
2. The conda Organization, in conjunction with our fiscal sponsor, then have the right to sublicense the trademarks to other projects, subject to specific limitations: The conda Organization may not degrade the distinctiveness of _licensed_ trademarks, or use _licensed_ trademarks to disparage or misrepresent the assigner. _Transferred_ trademarks are completely controlled by the conda Organization and its fiscal sponsor.
3. The [Steering Council](#steering-council) then makes trademark decisions, including the ability to revoke previously assigned trademarks, subject to agreed upon restrictions, and coordinates efforts with our fiscal sponsor.

We have guidelines for making decisions about conda Organization trademarks:

1. The project should be open source with a permissive license. [From OSI](https://opensource.org/faq#permissive):

   > A "permissive" license is simply a non-[copyleft](https://opensource.org/faq#copyleft) open source license — one that guarantees the freedoms to use, modify, and redistribute, but that permits proprietary derivative works.

2. The project should be related to the conda ecosystem
3. The project should be not be overly grand in claiming namespace
4. The project should not make subjective claims in the chosen project name

Examples of project names that violate the 3rd and 4th guidelines are `conda Pro`, and `pets-dot-com-conda-saves-the-day`.

The conda Organization is in a particularly challenging situation here because the conda name and logo are obviously derived from the [Anaconda Inc.](https://anaconda.com/) name and logo. Several precedents guide us here: Projects like [conda-forge](https://conda-forge.org/) (name), [Bioconda](https://bioconda.org/) (name and logo) and [conda-lock](https://github.com/conda/conda-lock) (name) have been approved in the past.

## Incubation

All projects start their journeys in an experimental or unstable state. To this end, we delineate stable projects as living in the [`conda` GitHub organization](https://github.com/conda/). Therefore, projects new to the conda Organization and governance must begin their inclusion in the [`conda-incubator` GitHub organization](https://github.com/conda-incubator/). The barrier to entry for a project to be added to the incubator should be very low. A vote from the [Steering Council](#steering-council) is required to move a project from incubation to the main GitHub organization.

Any single member of the Steering Council may add a project to the incubator, given the knowledge and consent of the author(s) (see the [Steering Council documentation on voting](./steering-council/charter.md/#voting)). Members of the Steering Council that are sponsoring the incubation are responsible for ensuring that basic legal requirements have been met that allow for the incubation. For example, [trademark usage and license terms](#trademarks) must have been checked prior to incubation.
