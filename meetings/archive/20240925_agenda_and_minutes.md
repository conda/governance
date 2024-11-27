---
tags: [meeting-notes]
---
# 2024-09-25 Conda Community Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation    | GH Username      |
| ---------------------- | -------- | -------------- | ---------------- |
| Schuyler Martin        | SM       | Anaconda       | schuylermartin45 |
| Bianca Henderson       | BH       | Anaconda       | beeankha         |
| Marco Esters           | ME       | Anaconda       | marcoesters      |
| Ken Odegard            | KO       | Anaconda       | kenodegard       |
| Jonathan Helmus        | JH       | Anaconda       | jjhelmus         |
| Tania Allard           | TA       | Quansight Labs | trallard         |
| Klaus Zimmermann       | KZ       | Quansight      | zklaus           |
| Lilly Winfree          | LW       | Anaconda       | lwinfree         |
|                        |          |                |                  |

X people in total

## Introductions

- [] Lilly: new product manager for conda @ Anaconda
- [] Tania

## Announcements

- [ ] https://www.anaconda.com/blog/update-on-anacondas-terms-of-service-for-academia-and-research
- [ ] Mamba 2.0 final is out!
    - [ ] https://github.com/conda-forge/mamba-feedstock/pull/249#pullrequestreview-2328149170
    - [ ] https://medium.com/@QuantStack/introducing-mamba-2-0-0e8d5c6d1d0c
- [ ] Zulip chat trial period at conda.zulipchat.com
    - [ ] https://github.com/conda/communications/issues/29
    - [ ] Reach out for an invite if you are interested (specially if you are a SC member!)
- [ ] (conda) build tools meeting resuming soon!
    - [ ] Details: Every 2nd Thursday of the month at 4pm Coordinated Universal Time (UTC)
    - [ ] Working to add to [community calendar](https://conda.org/community/calendar)
    - [ ] Bring any discussion topics, questions, and announcements related to package building tools and practices (not restricted to conda-build)

## New Agenda Items

- [ ] Conda channel management epic making progress for upcoming conda 24.9.x release
    - [ ] https://github.com/conda/conda/issues/14217
    - [ ] https://github.com/conda/conda-standalone/pull/99
    - [ ] https://github.com/conda/constructor/pull/863
    - [ ] Miniconda and Anaconda Distribution will start shipping .condarc files in PREFIX with explicit `channels: [defaults]`.
- [ ] (WV) rattler-build / pixi build stuff happening
    - [ ] https://github.com/conda-forge/conda-forge-ci-setup-feedstock/pull/337 - last piece of the puzzle (for now)
    - [ ] https://github.com/prefix-dev/pixi/tree/feature/pixi-build (pixi build feature branch)
    - [ ] pixi global
- [ ] Blog post reviews pls: rattler moving to conda.org https://github.com/conda/conda-dot-org/pull/211