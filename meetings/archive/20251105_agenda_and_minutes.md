---
tags: [meeting-notes]
---
# 2025-11-05 Conda Community Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Daniel Ching           | DJC      | NVIDIA/cf    | carterbox        |
| Bas Zalmstra           | BZ       | Prefix.dev   | baszalmstra      |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp         |
| Ryan Keith             | RSK      | Anaconda     | ryanskeith       |
| Schuyler Martin        | SM       | Anaconda     | schuylermartin45 |
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

- [x] DJC: nvidia-virtual-packages
    - A conda virtual package plugin which detects the minimum CUDA architecture available on the system
    - Source: https://github.com/NVIDIA/nvidia-virtual-packages
    - RFC: https://github.com/conda-forge/conda-forge.github.io/issues/2623
    - Motivation: Deep learning packages often have minimum supported CUDA archs which don't align with the CTK
        - https://github.com/conda-forge/cudnn-feedstock/issues/124
        - https://github.com/conda-forge/flash-attn-feedstock/blob/b6e3742a7343268a33a285c593753fd49b46d268/recipe/meta.yaml#L23
    - Motivation: Would be possible to break large binaries into smaller variants along CUDA arch
    - Cheng sponsoring incubation: https://github.com/conda/governance/issues/308
- [X] JRG: A bunch of [foundational CEPs](https://github.com/conda/ceps/pulls?q=sort%3Aupdated-desc+is%3Apr+is%3Aopen+author%3Ajaimergp) ready for comments.
    - How to handle the vote? Thinking of establishing a temporary committee that the SC delegates to for this unusual amount of inter-related CEPs that hopefully make it easier for innovation CEPs.
        - Cheng: supportive of the idea.
- [X] BZ: [FOSDEM2026](https://fosdem.org/2026/) (Brussels, Jan 31st - Feb 1st) can we meeting as at least the steering council face to face?
    - Will also have a Packaging Dev Room (Sat. morning)
    - WV: Really liked last year, different from Scipy, bigger, very open-sourcy.
    - Action item: Open discussion on Zulip to gather attention.
- [X] BZ: Conditional dependency support merged in rattler! Extras as well. Flags still pending. All under experimental features.
    - Need to be enabled in Python bindings.
    - Exposed in `rattler` binary.
    - Syntax as expressed in CEP so far, easy to change if needed. Most complex part was the solver (resolvo).
    - JRG: How costly would it be to port this to libsolv/libmamba?
        - BZ: libsolv technically supports conditional rules, so it should be doable. Depends on how libmamba is wrapping it, but probably more a "weeks effort" than a "days effort".
- [X] SM: New release of conda-recipe-manager.
    - New feature coming soon, might impact conda-build usage.
    - Trying to get into handling conda_build_config.yaml and variants.
