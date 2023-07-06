---
tags: [meeting-notes]
---
# 2023-07-05 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation       | GH Username      |
| ---------------------- | -------- | ----------------- | ---------------- | 
| Katherine Kinnaman     | KK       | Anaconda          | kathatherine     |
| Marius van Niekerk     | MvN      | Voltron Data / cf | mariusvniekerk   |
| Jaime Rodríguez-Guerra | JRG      | Quansight         | jaimergp         | 
| Bianca Henderson       | BH       | Anaconda          | beeankha         |
| Katherine Abrikian     | KCA      | Anaconda          | kalawac          |
| Jannis Leidel          | JL       | Anaconda/cf       | jezdez           |
| Marcel Bargull         | MB       | Bioconda/cf       | mbargull         |
| Jesse Wiles            | JWW      | Anaconda          | jessewiles       |
| Dave Clements          | DPC      | Anaconda          | tnabtaf          |
| Wolf Vollprecht        | WV       | prefix.dev        | wolfv            |
| Cheng H. Lee           | CHL      | Anaconda          | chenghlee        |

12 people in total

## Introductions

- No new attendees

## Announcements

- [x] (BH) Conda 23.7.0 and conda-build 3.26.0 release process will start this month!
- [x] (JRG) SDG Round 3 Call for Proposals Announcement: August 4, 2023

## New Agenda Items

- [x] (JRG) Starting a vote on two CEPs:
  - The "menuinst" CEP: https://github.com/conda-incubator/ceps/pull/8
  - The "run_exports" CEP: https://github.com/conda-incubator/ceps/pull/51
- [x] (JRG) Request incubation for conda-store
    - [x] JL: Relevant governance section: https://github.com/conda-incubator/governance/tree/f3c86238ade6008a2a374998fe2de30a13e10cb0#incubation
        - Steering council members do not need to request
- [x] (JL) Conda and the libmamba solver: Roll-out plan 2023
    - https://conda.org/blog/2023-07-05-conda-libmamba-solver-rollout/
    - Preinstalled in Miniconda et al by July
    - Conda libmamba solver is expected to be the default solver as of the September release, but the classic solver will not go away
    - Please share the blog post widely
- [x] (JL) Upcoming trial for Cirrus CI based macOS GitHub Actions runners for conda GH organization
    - https://github.com/apps/cirrus-runners
    - https://cirrus-ci.org/blog/2022/11/03/github-actions-on-m1-via-cirrus-runners/
    - Goal is to increase resources and make processes smoother
    - Costs will be covered by Anaconda-specific billing; once Numfocus / conda trademark issues sorted out, we can update our approach
    - Contact Jannis with any questions
- [X] (KCA) Shell plugin hook and plugins CEP for feedback: https://github.com/conda-incubator/ceps/pull/58
- [x] (WV) Bas Zalmstra for steering council?
    - Figure out schedule for meeting (adoodle.org, etc.), check conda incubator governance document for process: https://github.com/conda-incubator/governance#steering-council-membership
- [x] (JL) Steering council members - please update funding declarations via PR
    - Funding definition needs to be better defined, but where clear, please add
    - General update to governance, including clarification of 2-person funding rule, on Dave Clements' Q3 agenda
    - Contact Dave if you have input/questions.
- [x] (WV) [libsolv-rs](https://github.com/mamba-org/rattler/pull/243) is merged in [rattler](https://github.com/mamba-org/rattler/)!
    - https://ochagavia.nl/blog/the-magic-of-dependency-resolution/
- [x] (WV) Also would like to call a vote for the new recipe YAML format soon! 
- [ ] (JK) Anaconda.org metadata updates
    - JK was absent from meeting and put this on the agenda prior to the start of the meeting. These points seem to be suggestions and were discussed during the meeting as best as possible, given JK's absence
    - [x] `license_url` not showing up for packages ( https://github.com/conda/infrastructure/discussions/739 )
        - (JWW) Fix has been merged; expected in next release
    - [x] Revisit `recipe_url` idea ( https://github.com/conda/conda-build/pull/2489 )
        - additional metadata that anaconda.org could support
        - (MB) this would be nice not only for checking how things are built but also for building packages from multiple channels
    - [x] More options to sort and filter packages (e.g., subdir, build string, etc.)
        - (KK) It would be good to add ticket to conda infrastructure repo
        - (JWW) Will take this on as action item
        - (JRG) Maybe related: https://github.com/conda-forge/conda-smithy/pull/1577
    - [ ] The `anaconda copy` command with the `--replace` flag replaces both the metadata and the destimation package.
        - The docs indicate it should only replace the metadata in one spot (https://github.com/Anaconda-Platform/anaconda-client/blob/master/binstar_client/commands/copy.py#L67C5-L67C111) but the error message here (https://github.com/Anaconda-Platform/anaconda-client/blob/master/binstar_client/commands/copy.py#L42) indicates it should overwrite the package too.
        - We'd like an option to only replace the metadata on the package landing page.
- [x] (CHL) SciPy 2023 Sprint
    - No confirmation per se, but "we aren't planning to reject any projects that submit an application prior to the conference"