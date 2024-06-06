---
tags: [meeting-notes]
---
# 2024-06-05 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Jannis Leidel          | JL       | Anaconda/conda/cf | jezdez      |
| Marco Esters           | ME       | Anaconda     | marcoesters      |
| Filipe Fernandes       | FF       | conda-forge  | ocefpaf          |
| Bianca Henderson       | BH       | Anaconda     | beeankha         |
| Wolf Vollprecht        | WV       | prefix.dev   | wolfv            |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp         |
| Nichita Morcotilo      | NM       | prefix.dev   | nichmor           |
| Marcel Bargull         | MB       | Bioconda/cf  | mbargull         |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Dasha Gurova           | DG       | Anaconda     | dashagurova      |
| Bas Zalmstra           | BZ       | prefix.dev   | baszalmstra      |

11 people in total

## Introductions
- [ ] Aaron Opfer, Python dev (Chicago Trading Company)

## Announcements


## New Agenda Items


- [x] (WV) [rattler-build](https://github.com/prefix-dev/rattler-build) shaping up
    - [x] [nushell support](https://github.com/prefix-dev/rattler-build/pull/907)
    - [x] files selection support
        - [x] Equivalent in conda-build: https://github.com/conda/conda-build/pull/5216
    - [x] [experimental cache support](https://github.com/prefix-dev/rattler-build/pull/898)
        - [x] JL: Not sure about the name of `cache`.
        - [x] JRG: Maybe `pre-build`?
    - [x] WV: Good time to check the open ceps for comments: https://github.com/conda/ceps/pulls/wolfv
- [x] (WV) reproducible builds effort also shaping up
- [x] (WV) resolvo improvements for up to 10x faster resolves (vs libsolv)
    - [x] just need to finish the error reporter
- [x] (JL) made call for rattler-build focused trial (not just toying!) within Anaconda
    - [x] Any rattler-build starting guide available?
    - [x] Onboarding for conda-build user
- [ ] (JRG) A round of informative CEPs just dropped. [`explicit.txt`](https://github.com/conda/ceps/pull/79), [`environment.yml`](https://github.com/conda/ceps/pull/81), [`MatchSpec` grammar](https://github.com/conda/ceps/pull/82).
    - [ ] I'd like to end up with something like [what packaging.python.org has](https://packaging.python.org/en/latest/specifications/). Possibly with some elements from OpenContainers too ([runtime spec](https://github.com/opencontainers/runtime-spec/blob/main/spec.md), [image-spec](https://github.com/opencontainers/image-spec/blob/main/spec.md), [distribution-spec](https://github.com/opencontainers/distribution-spec/blob/main/spec.md))
- [ ] (JL) Governance FYIs and ideas:
    - [ ] New discussion: "conda maintainers" team to replace legacy "conda-core" catch-all
        - [ ] feedback welcome
        - [ ] @dholth, JL, JRG discussed whether to include conda-package-streaming, conda-package-handling in that as well
        - [ ] https://github.com/conda/conda/issues/13526
    - [ ] FYI: Passed vote and created new "CLA Reviewers" team
        - [ ] https://github.com/conda/governance/issues/136
    - [ ] Idea: A technical review group, to streamline deep work on standard CEPs
        - [ ] this was tried before, we didn't agree on a format
        - [ ] How can we help the steering council to review and vote on CEPs that are outside their skillset?
