---
tags: [meeting-notes]
---
# 2025-12-03 Conda Community Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Ryan Keith             | RSK      |  Anaconda    | ryanskeith       |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp         |
| Jannis Leidel          | JL       | Anaconda/cf  | jezdez           |
| Sylvain Corlay         | SC       | QuantStack   | sylvaincorlay    |
|                        |          |              |                  |
|                        |          |              |                  |
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

- [X] Future of conda-build discussion
    - Discussing options about way forward
    - JL: Beyond salvation, don't think about refactoring bits or uncoupling conda <> condabuild
    - JRG: Proposal: Freeze into conda-build-standalone and distribute a conda subcommand plugin that forwards to conda-build-standalone or rattler-build depending on the recipe format
    - RSK: One case for conda-build need is there may not be viable v1 solutions to a v0 recipe.
- [X] JK: Recent outage
    - https://github.com/conda/infrastructure/issues/1254
    - Want to understand: Are we close to hitting a limit due to increasing usage? Or was this a spurious error?
        - JL/CHL: Still in touch with Cloudflare to complete post-mortem. This was on Cloudflare's side of things.
- [X] JK: Best way to collect download statistics _today_
    - https://github.com/conda-incubator/condastats/issues/23
    - Dasha: Great topic. Planning to attend next CF meeting with Lilly to discuss improvements around this idea.
    - JK: Very happy to see there are plans to improve it! What about existing data?
        - JL: Need to get in touch with Nick Cappadona to find the best strategy.
    - JRG: Raw parquet data is still available and being published, right?
        - JL: Yes.
        - Potential solution for needs at https://github.com/conda-incubator/condastats/issues/23#issuecomment-3596372808
    - JL: The need for this type of dashboard is obvious; e.g. https://uwekorn.com/2025/12/01/py314-availability-on-conda-forge.html
- [X] JL: Sharded repodata launch for conda-forge on anaconda.org tomorrow!
    - Blog post draft: https://github.com/conda/conda-dot-org/pull/297
    - SC: Planning to implement it in core mamba too. Let's stay in touch so we don't break anything.
- [X] SC: Good progress in WASM channels. Interested in seeing this succeed for the whole conda ecosystem. Maintaining emscripten-forge on their own, but wants to add it to conda-forge.
    - Related issue: https://github.com/conda-forge/conda-forge.github.io/issues/2244
    - SC: Main blocker used to be recipe.yaml support. Allowed as a valid subdir now in `conda` (https://github.com/conda/conda/pull/13095, https://github.com/conda/conda/pull/13962). API breakages not as common as expected (mostly IO bits); might need some sort of epoch package to track bumps. Main interest is to use the feedstock maintenance approach to leverage community resources instead of having a small team maintain the whole emscripten-forge on their own.
    - JK: Linux ARM support in conda-forge was not initially there. Started as experiments by different people, and eventually became part of conda-forge. That model can still be useful here, and replicated. Can use a different channel label while things are prototyped.
- [X] CHL: Should this be our last meeting of the year? Or should we have a meeting on Dec 17th?
    - JRG: Personally planning to attend next CF meeting (Dec 10th) and then call it a year.
    - Decision: No more conda community calls in December. Will come back in January as a unified conda + conda-forge community call!
