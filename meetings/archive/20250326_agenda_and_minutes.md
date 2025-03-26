---
tags: [meeting-notes]
---
# 2025-03-26 Conda Community Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
|                        |          |              |                  |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp         |
| Jonathan Helmus        | JJH      | Anaconda     | jjhelmus         |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Wolf Vollprecht        | WV       | prefix.dev   | wolfv            |
| Marco Esters           | ME       | Anaconda     | marcoesters      |
| Dasha Gurova           | DG       | Anaconda     | dashagurova      |
| Jannis Leidel          | JL       | Anaconda/cf  | jezdez           |
| Dawn Wages             | DW       | Anaconda     | dawnwages        |
| Sophia Castellarin     | SC       | Quansight/cf | soapy1           |

10 people in total

## Introductions

- [x] Dawn Wages (new Director of Community and Developer Relations at Anaconda)

## Announcements

- [x] JJH: [conda-managed-env](https://github.com/conda-forge/conda-managed-env-feedstock) : conda package which prevents pip/uv from modifying an environment. Accomplished by adding `EXTERNALLY-MANAGED` file to the environment.
- [x] Jaime: constructor release [3.11.3](https://github.com/conda/constructor/releases/tag/3.11.3)
- [x] JL: conda/conda-build March release cycle
- [x] JL: New conda-maintainers members: George Lorch (EM at Anaconda) and Jonathan Helmus!

## New Agenda Items

- [x] Jaime: CEPs to vote
    - [x] Before Apr 2nd: Frozen environments, https://github.com/conda/ceps/pull/99
    - [x] Before Apr 2nd: Text spec input files (@EXPLICIT), https://github.com/conda/ceps/pull/79
    - [x] Coming soon, environment.yml: https://github.com/conda/ceps/pull/81
- [X] Jaime: conda/schemas is live again: https://github.com/conda/schemas, https://schemas.conda.org/. Contains menuinst schemas, 
- [x] WV: Abi check tool prototype
- [x] WV: `pixi shell` now also sources autocompletion files
