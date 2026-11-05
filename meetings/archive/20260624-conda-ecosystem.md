---
tags: [meeting-notes]
---
# 2026-06-24 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

1. DJC: Daniel Ching (@carterbox), NVIDIA, CF/SR
1. DY: Dan Yeaw (@danyeaw), Anaconda.
1. JK: John Kirkham (@jakirkham), NVIDIA/CF/CFC
1. CHL: Cheng H. Lee (@chenghlee), Anaconda, C/SC, CF/C
1. SC: Sophia Castellarin (@soapy1), Openteams

## New agenda items

- [x] (DJC) (Solver and virtual packages in run_constrained)[https://github.com/conda/conda/issues/10803]
    - Any updates on accepting fixes to this bug?
    - (DY) Timing on classic solver isn't ideal, since we're in the process of splitting the classic solver out of the core conda code base.  Would like to avoid any major changes to the classic solver right now.
    - (DJC) Have proposed fixes for both classic and libmamba solver; would like at least one solver that doesn't have this bug.
    - (DY) Planning on releasing libmamba this week; could consider holding off until PR fixing this bug gets in.
    - (DJC) Related: how would I prevent installations of packages using solvers that have this bug? Could we, e.g., have a depends on `__conda >=<some version>`?
        - (CHL): Maybe? I'm not really sure what the behavior would be if trying to install into a non-`base` environment.
        - Unclear what the original purpose(s) of the `__conda` virtual package was
        - (JK) How would other package managers implement similar solutions?
