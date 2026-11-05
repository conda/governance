---
tags: [meeting-notes]
---
# 2026-02-25 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

1. DY: Dan Yeaw (@danyeaw), Anaconda
1. KZ: Klaus Zimmermann (@zklaus), Quansight
1. TH: Travis Hathaway (@travishathaway), Anaconda
1. JRG: Jaime Rodríguez-Guerra (@jaimergp), Quansight, CF/C, C/SC
1. WV: Wolf Vollprecht (@wolfv), prefix.dev, CF/C, C/SC
1. CHL: Cheng H. Lee (@chenghlee), Anaconda, CF/C, C/SC

## Announcements

- [X] JRG: @ conda/steering-council, please review [open vote for foundational CEPs](https://github.com/conda/ceps/issues/147#issuecomment-3908100064). Deadline is next Monday EOD AoE (March 2nd). Jaime available for questions at any point if needed. Reach out on Zulip.
- [X] WV: rattler-build release 0.58 being pushed out
    - Big refactor, also of the parser (stricter now, supported by a lot of testing in real feedstocks). Brand new Python bindings, sigstore, cache stage, and many bugfixes
    - Also new Pixi release yesterday.
    - Working on signing Pixi releases for Windows.
    - Might integrate artifact signing directly in rattler-build.

## New agenda items

- [x] JRG: conda-forge soon to have access to extended concurrency in Github Actions. Still figuring out how to prevent self-DOS for our infra and automation.
