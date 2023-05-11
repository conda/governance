---
tags: [meeting-notes]
---
# 2023-05-10 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation    | GH Username      |
| ---------------------- | -------- | ---------------|------------------|
| Jannis Leidel          | JL       | Anaconda/conda | jezdez           |
| Bianca Henderson       | BH       | Anaconda       | beeankha         |
| Travis Hathaway        | TH       | Anaconda       |                  |
| Filipe Fernandes       | FF       | conda-forge    | ocefpaf          |
| John Kirkham           | JK       | NVIDIA/cf      | jakirkham        |
| Jesse Wiles            | JW       | Anaconda       | jessewiles       |
| Katherine Kinnaman     | KK       | Anaconda       | kathatherine     |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf   | jaimergp         |
| Katherine Abrikian     | KCA      | Anaconda       | kalawac          |
|                        |          |                |                  |
|                        |          |                |                  |

9 people in total


## Introductions

- [ ]

## Announcements

- [x] (JL) Vote running to graduate conda-dot-org project from conda-incubator to conda main GitHub organization: https://github.com/conda-incubator/conda-dot-org/issues/110
- [x] (BH) May releases (for [conda](https://github.com/conda/conda/milestone/60) and [conda-build](https://github.com/conda/conda-build/issues/4859)) will be getting worked on
- [x] (KK) GSoD Tech Writer chosen for conda.org!
    - https://github.com/conda-incubator/conda-dot-org/discussions/125


## New Agenda Items

- [x] (JK) Updates on Conda org setup?
- [x] (JK) Conda-build recipe format updates
    - https://github.com/prefix-dev/rattler-build#the-recipe-format
    - (JRG) https://gist.github.com/jaimergp/3a1dcdf524583a93529f0d122e61856a
    - (JL) Standardize what we have. Then evolve that standard forward to one of these choices
    - (JL) Plugins for formats?
- [x] (JK) Conda-build multiple format outputs / conversion
    - example right now: wheels
        - https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html#output-type
        - (also related) https://github.com/conda-incubator/conda-press
    - some other package formats come up: RPMs
        - https://github.com/pelson/conda-rpms
    - Maybe overlaps with packaging roundtable discussion?
    - JL: could be a plugin API to maintain separately?
    - JL: WebAssembly also came up
    - JL: Maybe plugin framework (like in Conda) could be used here?
    - JK: conda pipbuild
        - (removed) https://github.com/conda/conda-build/blob/01bd8b4ac7d781cf9846a82708ffbec68832d7f5/conda_build/main_pipbuild.py
- [x] (JRG) [conda/schemas revamp](https://github.com/conda/schemas/pull/26)
- [x] (JRG) EuroScipy 2023 @ Basel: [Maintainers track](https://www.euroscipy.org/2023/maintainers.html).
