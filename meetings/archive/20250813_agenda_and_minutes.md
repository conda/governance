---
tags: [meeting-notes]
---
# 2025-08-13 Conda Community Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Schuyler Martin        | SM       | Anaconda     | schuylermartin45 |
| Travis Hathaway        | TH       | Anaconda     | travishathaway   |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Lilly Winfree          | LW       | Anaconda     | lwinfree         |
| Ryan Keith             | RSK      | Anaconda     | ryanskeith       |
| Marco Esters           | ME       | Anaconda     | marcoesters      |
| Jaime Rodríguez-Guerra | JRG      | Quansight    | jaimergp         |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |

X people in total

## Introductions

- [ ]

## Announcements

- [x] SM: `conda-recipe-manager` (CRM) [v0.6.1](https://github.com/conda/conda-recipe-manager/releases/tag/v0.6.1) Released last week
    - Contains more parsing bug fixes
    - The next version of CRM will (probably) contain:
        - Significant logging improvements
        - A series of wrapped parsing exceptions
        - More parsing bug improvements
- [x] SM: Filed a request to form a CRM sub-team: https://github.com/conda/governance/issues/270
    - Similar to the sub-team that was recently formed for Conda development
    - Will allow others to manage the OSS CRM project board

## New Agenda Items

- [X] JRG: Discourse spam problem
- [x] TH: Label incoming issues for `source::*` in conda org
    - https://github.com/conda/infrastructure/issues/1190 <-- infra issue
    - Helps us figure out where an issue comes from
    - Keeps things organized
- [X] RSK: Proposal to move conda-pack from the constructor team to the conda-maintainers team
- [x] WV: requested_specs vs requested_spec
- [x] WV: work continuing on extras + conditional dependencies implementations
- [x] TH: https://conda.zulipchat.com/#narrow/channel/457607-general/topic/conda.20roadmap.20format/with/534253885