---
tags: [meeting-notes]
---
# 2026-03-04 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

1. JRG: Jaime Rodríguez-Guerra (@jaimergp), Quansight, CF/C, C/SC.
1. CHL: Cheng H. Lee (@chenghlee), Anaconda, CF/C, C/SC
1. DY: Dan Yeaw (@dyeaw), Anaconda
1. LW: Lilly Winfree (@lwinfree), Anaconda
1. WV: Wolf Vollprecht (@wolfv), prefix.dev, CF/C, C/SC
1. PZ: Pavel Zwerschke (@pavelzw), QuantCo
1. DH: Daniel Holth (@dholth), Anaconda 

## Announcements

- [x] JRG: Foundational CEPs [passed](https://github.com/conda/ceps/issues/147). All of them! Congratulations! CEPs 29-38 are now a reality.
- [x] WV: rattler-build release out!
    - Huge re-factor; more crates and Python bindings
    - Powershell should be working again?
    - Does it parse v0 recipes? No, but maybe you do something with conda-recipe-manager.

## New agenda items

- [x] JRG: Sprints at PyCon DE (Darmstadt, Germany, Apr 13): any conda or conda-forge projects you'd like to see cover. Please check https://conda.zulipchat.com/#narrow/channel/457607-general/topic/PyCon.20DE.202026/with/577300698 and drop your comments :pray: 
- [x] LW & DG: Channel notices 
    - [CEP 6](https://github.com/conda/ceps/blob/main/cep-0006.md)
    - Example issue: https://github.com/conda/infrastructure/issues/1099
    - Are there other channel maintainers who would like to make use this capability? If so, please comment in the `conda/infrastructure` issue above.
    - (IF) Are these notices channel-wide or at a package-level?
        - (CHL) Currently, specification is at a per-channel level
        - (IF) Package-level notices could be useful, e.g., to let users know about unmaintained packages that should not be used or help out with maintenance
        - (WV) prefix website adding concept of a parent channel; e.g., so `bioconda` maintainers can notify users need that they also need `conda-forge`
    - (LW) User research suggests that users struggle with the concept of channels.
        - (DY) Should channels have that information like parent channels in repodata? Would that need a CEP?
        - (WV) Probably, but may be better as another file.
        - (IF) Concept of parent channel could be done today using `custom_multichannel`
        - (DG) Would likely face challenges getting users to actually make that change
- [x] DH: Would like to call for a vote on conda deprecation policy + API conventions [CEP](https://github.com/conda/ceps/pull/143)
