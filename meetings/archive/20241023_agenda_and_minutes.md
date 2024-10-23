---
tags: [meeting-notes]
---
# 2024-10-23 Conda Community Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Schuyler Martin        | SM       | Anaconda     | schuylermartin45 |
| Marius van Niekerk     | MvN      | Voltron Data / CF            | mariusvniekerk                 | 
| Jaime Rodríguez-Guerra | JRG      | Quansight    | jaimergp         |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Filipe Fernandes       | FF       | conda-forge  | ocefpaf          |
| John Kirkham           | JK       | NVIDA/cf     | jakirkham        |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |

X people in total

## Introductions

- [ ]

## Announcements

- [x] [Conda Recipe Manager](https://github.com/conda-incubator/conda-recipe-manager) is expanding into other terrirtory
    - [x] Recipe Bumper
    - [x] Dependency work

## New Agenda Items

- [ ] (DG) PyTorch channel announcement: https://github.com/pytorch/pytorch/issues/138506
    - [ ] `condastats` seems to be reporting inaccurate download numbers
    - [ ] JRG: Surprisingly low given the amount of GH Search results for [`pytorch` channel mentions in `environment.yml` files](https://github.com/search?q=%2Fchannels%3A%5Cn*%5Cs%2B-+pytorch%2F+path%3Aenvironment.y*ml&ref=opensearch&type=code)
    - [ ] JK: Added a comment here: https://github.com/ContinuumIO/anaconda-package-data/issues/45#issuecomment-2433454611
- [ ] (DG) Status of Zulip transition?
    - [ ] JRG: [Opened draft CEP](https://github.com/conda/ceps/pull/92). No comments so far. Planning to call a vote once the [equivalent CFEP](https://github.com/conda-forge/cfep/pull/54) passes for conda-forge (scheduled Oct 31st).
    - [ ] DG: Willing to help if needed.
- [ ] (postponed) JRG: `conda/conda-launchers`: build on win-arm64 and codesign it?
    - See conversation at https://github.com/conda-forge/conda-forge.github.io/issues/1940#issuecomment-2413768986