---
tags: [meeting-notes]
---
# 2024-04-24 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Bianca Henderson       | BH       | Anaconda     | beeankha         |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Paul Yim               | PY       | Anaconda     |                  |
| Filipe Fernandes       | FF       | conda-forgte | ocefpaf          |
| Dasha Gurova           | DG       | Anaconda     |    dashagurova   |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp         |
| Klaus Zimmermann       | KZ       | Quansight    | zklaus           |
|                        |          |              |                  |
|                        |          |              |                  |

9 people in total

## Introductions

- [ ]

## Announcements

- [x] (BH) May 2024 releases of [conda](https://github.com/conda/conda/milestone/68) + [conda-build](https://github.com/conda/conda-build/milestone/40) will be under way soon!
- [x] (CHL) Some of us (Bianca, Jannis, Cheng) will be at the Packaging Summit at PyCon US. Come join us.

## New Agenda Items

- [x] (JRG) General heads up: GHA `macos-latest` runner is slowly becoming macos-14, so watch your OSX pipelines as they will soon use ARM64 instead of Intel.
    - Also macos-13 (still Intel) doesn't bundle a Miniconda anymore, so make sure to update to the latest setup-miniconda to mitigate potential errors (about to cut a release now).