---
tags: [meeting-notes]
---
# 2026-05-27 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

1. DJC: Daniel J. Ching (@carterbox), NVIDIA, cf
1. JRG: Jaime Rodríguez-Guerra (@jaimergp), Quansight, CF/C, C/SC
1. SM: Schuyler Martin (@schuylermartin45), Anaconda
1. CHL: Cheng H. Lee (@chenghlee), Anaconda, CF/C, C/SC
1. TH: Travis Hathaway (@travishathaway), Anaconda
1. JS: Jakov Smolic (@jsmolic), Quansight
1. MRB: Matthew Becker (@beckermr), CF/C
1. JL: Jannis Leidel (@jezdez), Anaconda, CF/C, C/SC
1. SG: Shahaf Golan, JFrog Artifactory
1. JK: John Kirkham (@jakirkham), NVIDIA/CF/CFC


## Introductions

- [x] Shahaf Golan joins from JFrog, as the tech lead of the team that works on conda integrations in artifactory

## Announcements

- [X] [conda 26.5.1](https://github.com/conda/conda/issues/16140) with some bugfixes

## From previous meetings

_(see CHL's item below)_

## New agenda items

- [x] WV: Status of https://github.com/conda/ceps/pull/146? What's needed to call a vote?
    - Action items:
        - add free form field too in repodata_revisions, all optional
        - defer `url` inclusion after [security concerns with mirrors](https://github.com/conda/ceps/pull/146#issuecomment-4506425051) were raised (SG from JFrog was present, thanks!)
        - MRB also mentioned that we need to prevent packages from injecting `url` from `index.json`; indexers need to validate and reject keys not covered by the schema (especially if they are optional at the indexing level)
        - call a vote
- [x] TH: [Staged recipe dashboard](https://srdb.thath.net/) MVP
    - Demo time :tada:
        - Overview page
        - Scoreboard page
    - Roadmap: https://hackmd.io/@thath/Hy9iAvbeMg
    - What else would be useful? What does GitHub not do well that we can compensate for?
    - How do we measure when something is "ready for review"
    - Further statistics to track (average review time, time to first response, more?)
    - Summary of comments: Response was positive, received concrete feedback by DJC, MRB suggested it could be part of conda-forge.org website (JRG agrees but that comes with questions about database size and how to deploy it in production). TH to iterate on prototype phase for a bit before tackling that challenge.
- [x] SM: GHA CLA 404: https://github.com/conda/conda-recipe-manager-test-data/pull/8
    - GitHub API updated on 2026-03-10 | [Endpoint Docs](https://docs.github.com/en/rest/commits/statuses?apiVersion=2026-03-10#create-a-commit-status)
    - Token problem as 404 instead of 403?
- [x] CHL: (About hardcoded activation paths in conda, in the context of "more unixy Cpython for Windows" CFEP) Did we write CEPs for all the other magic strings inside conda?. Thing about making these sort of issues into CEPs is that it would force what are essentially conda-forge's and Anaconda's conventions on all channels, which is something we as an ecosystem could do, but we should be deliberate about it. (Might not make that big a difference practically speaking, since such conventions are already hard-coded into conda & friends in various ways.)
    - From Zoom chat in the last meeting. Came up as a thought regarding msys2 and a more UNIX-y layout for Python discussion
    - E.g., https://github.com/conda/conda/blob/a4b150a22c4d5739db794d6cf7f56d977c5e0f87/conda/activate.py#L640-L644 covered by [CEP 32](https://github.com/conda/ceps/blob/main/cep-0032.md#activating-and-deactivating-an-environment).  But we have various strings in, e.g., `conda.base.constants`.
    - (JRG) Agreed, we should codify these magic strings somehow, either in CEPs or in the schema documentation.
- [x] JL: Feedback on https://github.com/conda/ceps/pull/154?
    - I'd like to get back to implementation for conda and mamba
    - Any major concerns, especially from prefix.dev given their implementation?
- [x] WV: PURL & CVE dashboard for conda-forge: https://prefix-dev.github.io/purl-associator/
    - JRG: [sig-purls](https://github.com/conda-incubator/sig-purls) repo for everything PURL in conda ecosystem!
    - JL (in chat): [...] that’s in prefix-dev right now, any plans to move that into conda-forge org?
        - consensus: fine to have it in prefix-dev while prototyping, eventually needs to move to a channel controlled and CEP approved metadata source (e.g. repodata.json via https://github.com/conda/ceps/pull/63)
- [x] WV: quarantine for conda-forge on prefix.dev mirror [to be able to deal with potential ongoing supply chain attacks]
    - MRB (in chat): For conda-forge, please report items here: https://github.com/conda-forge/security
- [x] WV: Sovereign Tech Agency application submitted for security improvements to conda-forge; shared in conda-forge/core chat for details.
