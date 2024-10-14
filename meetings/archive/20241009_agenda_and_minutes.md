---
tags: [meeting-notes]
---
# 2024-10-09 Conda Community Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
|                        |          |              |                  |
| Filipe Fernandes       | FF       | conda-forge  | ocefpaf          |
| Jannis Leidel          | JL       | Anaconda     | jezdez           |
| Matthew R Becker       | MRB      | conda-forge  | beckermr         |
| Schuyler Martin        | SM       | Anaconda     | schuylermartin45 |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Marco Esters           | ME       | Anaconda     | marcoesters      |
| Wolf Vollprecht        | WV       | prefix.dev   | wolfv            |
| John Kirkham           | JK       | NVIDIA/cf    | jakirkham        |
| Lilly Winfree          | LW       | Anaconda     | lwinfree         |
| Bianca Henderson       | BH       | Anaconda     | beeankha         |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |

X people in total

## Introductions

- [ ]

## Announcements

- [x] (JL) [site-packages path in repodata.json CEP](https://github.com/conda/ceps/pull/90) up for vote

## New Agenda Items

- [ ] (WV) rattler-build / v1 recipe being rolled out in conda-forge
    - Is there a way to tell if a package was built using `rattler-build`, rather than `conda-build`? Yes; output package will not contain certain files in the `info/` directory.
    - possible next steps? - end to end testing of select number of rattler-built packages 
- [ ] (WV) pixi global getting a huge makeover
- [x] (JL) ABI3 CEP, coordination between distros
    - [ ] https://github.com/conda/ceps/pull/86
- [ ] 
