---
tags: [meeting-notes]
---
# 2024-11-06 Conda Community Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Ruben Arts             | RA       | prefix.dev   | ruben-arts       |
| Bas Zalmstra           | BZ       | prefix.dev   | baszalmstra      |
| Filipe Fernandes       | FF       | conda-forge  | ocefpaf          |
| Marco Esters           | ME       | Anaconda     | marcoesters      |
| Wolf Vollprecht        | WV       | prefix.dev   | wolfv            |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp         |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Klaus Zimmermann       | KZ       | Quansight    | zklaus           |
| John Kirkham           | JK       | NVIDA/cf     | jakirkham        |
| Dasha Gurova           | DG       | Anaconda     | dashagurova      |

15 people in total

## Introductions

- [ ]

## Announcements

- [X] BZ/WV: CEP17 (python site-packages) implemented in rattler(/pixi) and rattler-build.
    - [ ] https://github.com/conda/ceps/blob/main/cep-0017.md
    - [ ] JL: support in conda/conda-build wil come in 24.11.0

## New Agenda Items

- [X] JRG: win-arm64 support and `conda/conda-launchers`: build on win-arm64 and codesign it?
    - See conversation at https://github.com/conda-forge/conda-forge.github.io/issues/1940#issuecomment-2413768986, issues at https://github.com/conda/conda-launchers/issues
- [X] JRG: `conda/ceps` now published in conda.org: see https://github.com/conda/conda-dot-org/pull/220
- [X] DG: Zulip CEP: https://github.com/conda/ceps/pull/92
    - conda-forge already moved: https://conda-forge.zulipchat.com/stats
    - Action item: call the vote
- [X] WV: conda-rattler-solver making some progress
    - https://github.com/jaimergp/conda-rattler-solver/pull/1
- [X] WV: rattler-build 0.29 release
- [X] WV: sharded repodata almost available on prefix.dev
- [X] WV: trusted publishers available on prefix.dev
- [X] JK: Download statistics?
    - https://github.com/ContinuumIO/anaconda-package-data/issues/45
    - https://github.com/ContinuumIO/anaconda-package-data/issues/57
    - CHL: Will talk to the team who works on this about these issues.
    - JL: Data team is still working on it, found inconsistencies in the data, backfill TBD
- [X] JK: Change default package format to `.conda`
    - https://github.com/conda/conda-build/issues/5183
    - JRG to create proposal PR in conda-build
- [X] DG: How can Anaconda help with the pytorch feedstock? CI resources, developer resources?
    - WV: Prefix paying for the Windows CI resources. Help with developer time higher priority. https://github.com/conda-forge/pytorch-cpu-feedstock/pull/288
    - JRG: Consolidate all communication in one central place. Possibly the conda-forge feedstock.
    - DG: Dan (Anaconda) interested in helping out (e.g. https://github.com/conda-forge/pytorch-cpu-feedstock/pull/280)
    - JK: See issues at https://github.com/conda-forge/pytorch-cpu-feedstock/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22help%20wanted%22 and https://github.com/conda-forge/pytorch-cpu-feedstock/issues/268
- [X] JRG: Change time of this meeting?
    - General feeling: yes, let's run a poll.
    - JK: This is a good opportunity to make sure we capture good notes for folks that cannot make it to one of the meetings.
    - JRG: Can we use AI to transcribe what's being said and then use that as a support for the note taking / refinement?
        - Consensus: give it a try in next call after asking for consensus.
