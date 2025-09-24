---
tags: [meeting-notes]
---
# 2025-09-24 Conda Community Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Dan Yeaw               | DWY      | Anaconda     | @danyeaw         |
| Schuyler Martin        | SM       | Anaconda     | schuylermartin45 |
| Ruben Arts             | RA       | Prefix.dev   | @ruben-arts      |
| Marco Esters           | ME       | Anaconda     | @marcoesters     |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | @jaimergp        |
| Cheng H. Lee           | CHL      | Anaconda/cf  | @chenghlee       |
| Ryan Keith             | RSK      | Anaconda     | @ryanskeith      |
| Pavel Zwerschke        | PZ       | QuantCo      | @pavelzw         |
| Wolf Vollprecht        | WV       | prefix.dev   | @wolfv           |
| Jannis Leidel          | JL       | Anaconda/cf  | @jezdez          |

X people in total

## Introductions

- [X] DWY: Dan introduced himself, Eng Manager for conda OSS at Anaconda

## Announcements

- [ ]

## New Agenda Items

- [X] JRG: New two-year funding from STA.
    - https://github.com/Quansight-Labs/conda-ecosystem-sta-mgmt
- [X] RA: Updates on `pixi-build`
    - Example build backends: [Python](https://github.com/prefix-dev/pixi-build-backends/blob/main/crates/pixi-build-python/src/main.rs) (written in Rust), [ROS](https://github.com/prefix-dev/pixi-build-backends/blob/main/backends/pixi-build-ros/src/pixi_build_ros/ros_generator.py) (written in Python). There's also a backend for rattler-build ([example](https://github.com/prefix-dev/pixi/tree/main/examples/pixi-build/array-api-extra)).
- [X] SM: How to best communicate CEP vs rattler-build doc inconsistencies?
- [X] WV: rattler-build: allow lists in context and other CEP-14 changes
    - {%preview https://github.com/conda/ceps/pull/131 %}
    - {%preview https://github.com/conda/ceps/pull/110 %}
- [X] WV: rattler-build "cache" proposal progress
    - {%preview https://github.com/conda/ceps/pull/102 %}
- [X] DWY: conda roadmap {%preview https://github.com/orgs/conda/projects/22/views/15 %}
- [X] DWY: Developer docs / process updates
- [X] JRG: PEP 725 / 804 updates
    - https://discuss.python.org/t/103890
    - https://discuss.python.org/t/103891
