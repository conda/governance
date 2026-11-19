---
tags: [meeting-notes]
---
# 2026-11-11 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

<!-- Use this syntax:
* Initials: Full Name (@github-username), Affiliation.
* SD: Sam Doe (@samdoe), Company
-->

1. TH: Travis Hathaway (@travishathaway), Anaconda Inc.
1. CHL: Cheng H. Lee (@chenghlee), Anaconda, C/SC, CF/C
2. LH: Ludovic Henry (@luhenry), RISE/Qualcomm
3. ...

<!-- Delete sections that do not apply before committing to repo -->
<!-- Every agenda item must use the initials of the person adding the item -->


## Introductions

## Announcements

## From previous meetings

## New agenda items

- [x] (TH) conda-forge win-arm64 migration
    - Status here: https://conda-forge.org/status/migration/?name=supportwindowsarm64platform
    - Now that I have a win-arm64 laptop, I've been actively trying to submit PRs for win-arm64 compatibility
    - Anything I should be aware of as I attempt this mission?
- [x] (LH) conda-forge linux-riscv64 migration
    - Hardware is available but slow; faster hardware will come
    - Bigger feedstock are taking too long with native compilation
        - https://github.com/conda-forge/llvmdev-feedstock/pull/395
    - Default to native-compilation, and accept cross-compilation for bigger feedstock?
        - Acceptable, use native compilation as default, switch to cross-complation for bigger ones
        - Need to be mindful about overhead and usage, friction needs to be low; Will look at download numbers months/year down the line to re-assess

## Deferred to next meeting

- [ ] ...
