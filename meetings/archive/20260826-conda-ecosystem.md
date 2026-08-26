---
tags: [meeting-notes]
---
# 2026-08-26 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

1. TH: Travis Hathaway (@travishathaway), Anaconda
1. CHL: Cheng H. Lee (@chenghlee), Anaconda, C/SC, CF/C
1. BZ: Bas Zalmstra (@baszalmstra), Prefix.dev, C/SC, CF/C
1. LH: Ludovic Henry (@luhenry), Qualcomm / RISE
1. DY: Dan Yeaw (@danyeaw), Anaconda
1. JS: Jakov Smolic (@jsmolic), Quansight

## Announcements

- [x] CHL: Conda SC - starting vote on [PURL CEP](https://github.com/conda/ceps/pull/159)
- [x] TH: Cool dashboard focused on staged-recipe turn around times and other various statistics: https://nodtem66.github.io/cfsr-stats/

## New agenda items

- [x] (HV, in absentia) Go/no-go for dropping py3.10, migrating for 3.15:
  - https://github.com/conda-forge/conda-forge.github.io/pull/2923
  - https://github.com/conda-forge/conda-forge-pinning-feedstock/pull/8891
  - Feel free to modify/merge at will from my (=HV) side
  - (IF) Generally drop version to be EOL when RC1 of new version comes along; minimize strain on CI resources so we're not building for 6 Python versions
- [x] TH: [prototypefund.de](https://www.prototypefund.de/en/)
    -  Program partially funded by the German government (requires at least one team participant to have residency in Germany)
    -  Two tracks that could be interesting for funding conda-forge related projects:
        -  https://www.prototypefund.de/en/resilience
        -  https://www.prototypefund.de/en/innovation
    - Do others feel like conda-forge could be a good match for this program?
    - If so, would anyone be interesting in writing an application for this program together as a team?  (I think we could come up with some neat ideas!)
    - Application period is between `2026-10-01` and `2026-11-30`
- [x] BZ: Update on publishing conda-forge packages directly to prefix.dev
    - We are working on "groups". `conda-forge` will be a group that can host multiple channels. Core members will be added as owners to this group.
    - We have a prototype that allows copying packages from a URL into a channel. All using graphQL.
    - The call is async it returns a job that can be queried for changes or just left alone.
    - A temporary channel will be created e.g. `conda-forge/staging` to which we will copy the packages. If this all works as expected we can switch the mirroring.
    - The call requires the API key of a core member, this can be scoped to specificly this operation and only on this channel.
    - In the future a frontend is added to view job states.
- [x] LH: linux-riscv64 / libffi review
    - blocking many other feedstocks; how do we get it moving?
    - https://github.com/conda-forge/libffi-feedstock/pull/63 (just merged, thanks @isuruf!)
- [x] IF: rattler-build not running tests
    - https://github.com/prefix-dev/rattler-build/pull/2769
- [x] BZ: microrattler preview
    - A blazingly fast drop in replacement for `conda` but built natively in rust using rattler.
    - Will contribute to conda-incubator soon(TM).
