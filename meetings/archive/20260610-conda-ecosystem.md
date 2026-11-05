---
tags: [meeting-notes]
---
# 2026-06-10 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

1. JRG: Jaime Rodríguez-Guerra (@jaimergp), Quansight, CF/C, C/SC
2. WV: Wolf Vollprecht (@wolfv), prefix.dev
3. SM: Schuyler Martin (@schuylermartin45), Anaconda
4. PZ: Pavel Zwerschke (@pavelzw), QuantCo
4. IV: Ivan Dimitrov, QuantCo
5. CHL: Cheng H. Lee (@chenghlee), Anaconda, C/SC, CF/C
6. JL: Jannis Leidel (@jezdez), Anaconda, C/SC, CF/C
7. JK: John Kirkham (@jakirkham), NVIDIA/CF/CFC
8. JS: Jakov Smolic (@jsmolic), Quansight
9. DY: Dan Yeaw (@danyeaw), Anaconda
10. DG: Dasha Gurova (@dashagurova), Anaconda
11. DH: Daniel Holth (@dholth), Anaconda

## Introductions

- [X] Ivan Dimitrov, from QuantCo

## Announcements

- [X] @ conda/steering-council:
    - CEP 38 amendment: https://github.com/conda/ceps/pull/172
    - `indexed_timestamp` to start the vote soon: https://github.com/conda/ceps/pull/154
- [X] @ conda-forge/core:
    - Check your [helios votes](https://vote.heliosvoting.org) for staged-recipe member addition
    - CFEP for Unixy layout for Python on Windows: https://github.com/conda-forge/cfep/pull/65
- [X] Marcel Bargull recently went emeritus. Thank you on behalf of conda-forge/core and conda/steering-council! <3

## New agenda items

- [x] (JK) Solver and virtual packages in run_constrained
    - https://github.com/conda/conda/issues/10803
    - (JRG) conda-libmamba-solver changes very likely to go in, classic... needs a discussion.
    - (JL) Should we take this opportunity to remove the classic solver into a separate package?
        - (JK) Related issue Dan (DY) opened
            - https://github.com/conda/conda/issues/16185
    - (JRG) Yes, since we haven't maintained it in a while.
    - (CHL) Yes, espeically since we don't want to modify it to support the accepted repodata v3 CEPs
    - (JK) Current usage?
    - (JL) Queriable via user agent with `solver/classic`
    - (JRG) Note to self: check conda-rattler-solver for compatibility
