---
tags: [meeting-notes]
---
# 2025-05-21 Conda Community Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Schuyler Martin        | SM       | Anaconda     | schuylermartin45 |
| Jaime Rodríguez-Guerra | JRG      | Quansight/sc | jaimergp         |
| Marco Esters           | ME       | Anaconda     | marcoesters      |
| Michael Sarahan        | MCS      | NVIDIA/cf    | msarahan          |
| John Kirkham           | JK       | NVIDIA/cf    | jakirkham        |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |

X people in total

## Introductions

- [ ]

## Announcements

- [ ] (SM) Conda Recipe Manager (CRM) [0.5.1](https://github.com/conda/conda-recipe-manager/releases/tag/v0.5.1) is now available.
    - Has a handful of bug fixes for `crm convert`
    - `crm bump-recipe` will now attempt to auto-correct PyPi source URLs AND it will upgrade all PyPi URLs to use `pypi.org`
- [ ] (SM) Conda Recipe Manager has a new [protected branch](https://github.com/conda/conda-recipe-manager/tree/dev_v1_rust_parser) where we are starting to experiment building a faster V1 parser backed by Rust. No timelines or guarantees can be provided at this time.
    - JRG: Related thread: https://conda.zulipchat.com/#narrow/channel/471111-builds-tools/topic/Preferred.20YAML.20Parser.20for.20Rust.3F/with/519602815
- [ ] (JRG) [conda-rattler-solver plugin](https://github.com/conda-incubator/conda-rattler-solver) preview: `conda install -n base conda-forge::conda-rattler-solver` + `conda create --solver=rattler ...`. 

## New Agenda Items

- [ ] (SM) Thoughts on building a combined conda-forge/Anaconda linter written in Rust, powered by CRM's editing capabilities?
    - In other words, a linter that is capable of being configured to accept conda-forge rules and Anaconda rules that can auto-fix linting issues.
    - JRG: Related issue in conda-smithy: https://github.com/conda-forge/conda-smithy/issues/2234
- [ ] ...
- [ ] ...
- [ ] ...
- [ ] 
