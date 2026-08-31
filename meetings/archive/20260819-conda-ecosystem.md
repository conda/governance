---
tags: [meeting-notes]
---
# 2026-08-19 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

1. TH: Travis Hathaway (@travishathaway), Anaconda
1. SM: Schuyler Martin (@schuylermartin45), Anaconda
1. WV: Biker Wolf :bike: (@wolfv), Prefix.dev
1. DY: Dan Yeaw (@danyeaw), Anaconda
1. JL: Jannis Leidel (@jezdez)
1. CHL: Cheng H. Lee (@chenghlee), Anaconda, C/SC, CF/C
1. JK: John Kirkham (@jakirkham), NVIDIA, C/SC, CF/CFC
1. MRB: Matthew R. Becker, CF/C
1. LH: Ludovic Henry (@luhenry)

## Introductions

- [x] LH: Member of RISE (https://riseproject.dev; Linux Foundation project), focused on enabling Software Ecosystem on RISC-V; Working on linux-riscv64 migration

## Announcements

- [x] (TH) Requesting to join build-tools team (https://github.com/conda/governance/issues/429)
    - Emeritus rejoin possible? (follow up with this later)
    - Let's check out the build-tools team charter
    - Ongoing PR is going to list @travishathaway as emeritus conda/governance team YAMLs (the yamls and GitHub's team are currently out of sync)
    - JL: I’ve put in some effort into Jaime’s PR a while ago, so I think we should just get this merged if it helps to clarify the gaps in the governance process
- [x] Steering: Repodata v3 vote, last day: https://github.com/conda/ceps/pull/146
- [x] Steering: PURLs CEP RFC period ending: https://github.com/conda/ceps/pull/159
- [x] Core: Two membership requests for conda-forge core and staged-recipes, respectively. Please check [Helios](https://vote.heliosvoting.org).

## New agenda items

- [x] JL: Started working on conda-sigstore plugin
    - https://github.com/jezdez/conda-sigstore
    - Depending on https://github.com/conda/conda/pull/16518 draft
    - Discussion on exposing more information useful for this via prefix.dev: https://github.com/prefix-dev/prefix-dev/issues/94
    - Sigstore-related packages available on conda-forge!

- [x] JFrog Artifactory starting gradual roll process to support for conda repodata shards
    - Do clients have fallbacks for HTTP 401 and 404 errors? (Yes)

- [x] WV: RISC V Migration 
- [x] WV: Starting to roll out organizations on prefix
    - You might see more URLs like `prefix.dev/wolfv/foobar`, and we might introduce `@wolfv/foobar` syntax
- [x] WV: pixi script is a thing now
- [x] WV: rattler-build script env vars extraction - yes or no?
    - https://github.com/prefix-dev/rattler-build/pull/2748

- [x] WV: sigstore CEP kinda ready.
    - [x] CEP: https://github.com/conda/ceps/pull/142
    - [x] Security review being completed: https://github.com/sigstore/sigstore-rust 

- [x] WV: channel notices being rolled out as well
- [x] WV: conda-forge swag
    - [x] https://github.com/conda-forge/governance/issues/21
![img](https://github.com/user-attachments/assets/cc024df2-b541-4845-a40c-2d83c8ab3041)
    - [x] Perhaps we can use the notices to help spread the word to get more maintainers for conda-forge!
