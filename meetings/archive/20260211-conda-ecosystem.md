---
tags: [meeting-notes]
---
# 2026-02-11 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

1. JRG: Jaime Rodríguez-Guerra (@jaimergp), Quansight, CF/C, C/SC.
2. BM: Ben Moss.

## Announcements

- [X] JRG: [RFC period for foundationals standards CEPs](https://github.com/conda/ceps/issues/147) ending this week. Vote to start next Monday.

## New agenda items

- [X] BM: How to become more involved in conda-forge after contributing a few feedstocks?
    - JRG: Two good starting points:
        - Help out by reviewing recipe types you are familiar in staged-recipes (check "review request" threads in the General channel in Zulip)
        - Flag omissions / out-of-date pieces in documentation.

## Deferred to next meeting

- [ ] JRG (conda-forge): Idea to request [OSS sponsorship for blacksmith.sh](https://www.blacksmith.sh/pricing) runners.
- [ ] JRG: [Bug in CEP 19](https://github.com/conda/ceps/issues/150)
- [ ] DH: Plan to discontinue `current_repodata.json` on conda-forge; it can't be used by modern solvers and is slow to generate.
- [ ] DH: CEPs regarding development policy for the Python implementation of conda. 14-day comment period has elapsed for "[use Python API conventions in conda instead of deprecation policy](https://github.com/conda/ceps/pull/143)"; alternate new CEP "[retract deprecation policy; move policy to conda developer documentation](https://github.com/conda/ceps/pull/152)"
