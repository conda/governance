---
tags: [meeting-notes]
---
# 2026-05-13 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

1. JRG: Jaime Rodríguez-Guerra (@jaimergp), Quansight, C/SC, CF/C
1. TH: Travis Hathaway, TH (@travishathaway), Anaconda
1. CHL: Cheng H. Lee (@chenghlee), Anaconda, C/SC, CF/C
1. DY: Dan Yeaw (@danyeaw), Anaconda
1. AS: Ahmed Shifa

## Announcements

- [x] Recently closed votes, vote count and minting to take place tomorrow:
        - 2026-05-11: CEP [Conditional dependencies](https://github.com/conda/ceps/pull/164)
        - 2026-05-11: CEP [Optional dependency groups](https://github.com/conda/ceps/pull/165) (extras)
        - 2026-05-11: CEP [Simplified variant selection](https://github.com/conda/ceps/pull/166) (flags)
- [x] Recently closed CEP RFCs, vote may start soon:
        - 2026-05-12: https://github.com/conda/ceps/pull/151 (`url` field in repodata records)
        - 2026-05-12: https://github.com/conda/ceps/pull/154 (`indexed_timestamp` field in repodata records)
- [x] @ conda/steering-council, open votes:
        - 2026-05-13: Ongoing vote for graduation of 4 repos: https://github.com/conda/governance/issues/384
        - 2026-05-19: CEP [__cuda_arch](https://github.com/conda/ceps/pull/157)
- [x] @ conda/build-tools please vote for Jakov's request https://github.com/conda/governance/issues/383. Deadline 2026-05-14 23:59 UTC.

## New agenda items

- [x] AS: How does someone get started in open-source and the conda ecosystem? 
    - (TH) Contribute a package via conda-forge staged recipes
    - (DY) Work on the stuff that interests you; it's your free time.
    - (CHL) "Easy" way to start with the documentation (e.g., quick start guides) and reporting bugs.  There's a lot more to OSS contribution than "just" writing code.
    - (TH) Find ways to use conda, conda-forge to build `<your cool app>`.  So much more to conda ecosystem than just Python and Python packages.

## Deferred to next meeting

- [ ] TH: Ideas for better tracking staged-recipe reviews
    - [ ] [staged-recipe review dashboard](https://conda-forge.zulipchat.com/#narrow/channel/457337-general/topic/CHAOSS.20Metrics.20for.20staged-recipes.20proposal/with/593206687) - idea on conda-forge zulip
    - [ ] Would it help to create a special dashboard for us to track recipe reviews?
        - [ ] Score board to encourage reviewers
        - [ ] Clear goals for new reviewers to achieve
        - [ ] Seeing which pull requests have been waiting the longest
        - [ ] Organizing pull requests by responsible team 
