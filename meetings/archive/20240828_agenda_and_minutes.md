---
tags: [meeting-notes]
---
# 2024-08-28 Conda Community Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Filipe Fernandes       | FF       | conda-forge  | ocefpaf          |
| Jaime Rodríguez-Guerra | JRG      | Quansight    | jaimergp         |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Klaus Zimmermann       | KZ       | Quansight    | zklaus           |
| John Kirkham           | JK       | NVIDIA/cf    | jakirkham        |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |

X people in total

## Introductions

- [ ]

## Announcements

- [ ]

## New Agenda Items

- [X] (WV) Security Subteam formation
    - [ ] Goal: implement package signing (SigStore) and other state of the art technologies for conda packages
    - [ ] Apply for funding with e.g. OpenSSF
    - [ ] Wolf pushing for this to not miss potential funding opportunities
    - [ ] First step: create subteam by creating an issue in `conda/governance`
- [ ] (JK) Adding CLA files
    - https://github.com/conda/cla/pull/5
    - Next steps? How to sign from Nvidia?
    - Official source of truth would be really useful.
- [ ] (JK) Updating Conda's behavior with channels (like `defaults`)
    - https://github.com/conda/conda/issues/12356
    - https://github.com/conda-incubator/setup-miniconda/issues/207
    - https://github.com/conda/conda/issues/14178
    - JRG: `defaults` these days is opt-out. Should it be opt-in? IMO yes.
    - KZ: defaults should require authentication, that would allow tracking.
- [ ] (JK) Suppress Jinja errors in skipped conditions
    - https://github.com/conda/conda-build/pull/5458
- [ ] (JK) Conda GH permissions? Who should have access?
    - Are we able to add steering council members here?
    - https://github.com/conda/conda/issues/13526
- [ ] (JRG) Packaging Windows launchers.
    - [ ] Experiment at https://github.com/conda-forge/staged-recipes/pull/27419
    - [ ] Would be nice to have its own repo, similar to what conda/conda-standalone does
    - [ ] Name ideas? `conda-[python-]launchers`?
