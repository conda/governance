---
tags: [meeting-notes]
---
# 2026-08-05 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

<!-- Use this syntax:
* Initials: Full Name (@github-username), Affiliation.
* SD: Sam Doe (@samdoe), Company
-->

1. JRG: Jaime Rodríguez-Guerra (@jaimergp), Quansight, CF/C, C/SC
1. DY: Dan Yeaw (@danyeaw), Anaconda
1. DJC: Daniel Ching (@carterbox), NVIDIA, CF/SR
1. CHL: Cheng H. Lee (@chenghlee), Anaconda, C/SC, CF/C
1. JK: John Kirkham (@jakirkham), NVIDIA/CF/CFC
1. LW: Lilly Winfree (@lwinfree), Anaconda
1. MRB: Matthew R. Becker, CF
1. IF: Isuru Fernando (@isuruf), OpenTeams, CF/C
1. WV: Wolf Volprecht (@wolfv), Prefix.dev, CF/C, C/SC
2. SM: Schuyler Martin (@schuylermartin45), Anaconda
3. ...

<!-- Delete sections that do not apply before committing to repo -->
<!-- Every agenda item must use the initials of the person adding the item -->


## Introductions

- [ ] ...

## Announcements

<!-- New releases, upcoming changes, ongoing votes --->

- [x] CHL: Starting RFC period for [conda PURL CEP](https://github.com/conda/ceps/pull/159)
- [x] JRG: [Repodata v3 CEP](https://github.com/conda/ceps/pull/146) vote to start soon, please check your notifications
- [x] JRG: conda-smithy 2026.8.5 just released. [Big release with lots of changes](https://github.com/conda-forge/conda-smithy/releases/tag/v2026.8.5), including GHA as default Windows provider. Do ping if anything smells weird!
- [X] JRG: New `#review-requests` channel in conda-forge's Zulip.

## New agenda items

- [x] IF: Policy on licenses for minified javascript code.
    - License only included in the minified JS file itself, not in the info/ directory. Should we enforce putting them there too?
    - DJC: Enumerate everything in the SPDX expression?
    - IF: We don't do that with cargo-bundle-licenses, it becomes complex really quickly.
    - MRB: Reminder that our licensing metadata is only a best effort. It can go stale, incomplete.
    - JRG: Maybe drop a hint file in the licenses/ directory? "More license information may be available in minified JS code. Double check." or something?
- [x] DJC: cuda-arch meta-package design update
    - Defaults to lowest arch if `__cuda_arch` not installed by using variants with and without that virtual package.
    - https://github.com/conda-forge/cuda-arch-feedstock/pull/1
    - https://github.com/conda-forge/admin-requests/pull/2241
    - IF: Have we added the plugin as a requirement to conda on conda-forge?
        - JRG: Not yet, but can happen soon.
    - DJC: Based on feedback, I will revise the design to require `__cuda_arch` in all cases in order to install `cuda-arch` metapackages 
- [x] LW: Discussion wanted for planned improvements to conda-forge clone process on anaconda.org
    - ask: who wants to do some asynch review of the technical plan?
        - Jaime; should reach out to bioconda (Lilly to follow up); Lilly can also post on Zulip 
    - Anaconda developers working on this: Burak & Alex (Oleksandr)
- [X] WV: move to v1 in staged recipes? https://github.com/conda-forge/staged-recipes/pull/34414
    - 20%+ https://tdejager.github.io/are-we-recipe-v1-yet/
    - JRG: We can add a hint to the staged-recipes linter that goes away when a certain label is added?
    - WV: CFEP needed?
        - Consensus: not needed for a linter change
    - https://github.com/conda-forge/staged-recipes/pull/34414/

## Deferred to next meeting

- [ ] ...
