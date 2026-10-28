---
tags: [meeting-notes]
---
# 2026-09-30 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

<!-- Use this syntax:
* Initials: Full Name (@github-username), Affiliation.
* SD: Sam Doe (@samdoe), Company
-->

1. TH: Travis Hathaway (@travishathaway), Anaconda Inc.
1. DJC: Daniel Ching (@carterbox), CF/C, NVIDIA
1. WV: Wolf Vollprecht (@wolfv), CF/C, prefix.dev
2. 

<!-- Delete sections that do not apply before committing to repo -->
<!-- Every agenda item must use the initials of the person adding the item -->


## Introductions

- [ ] ...

## Announcements

<!-- New releases, upcoming changes, ongoing votes --->

- [ ] TH: I got a shiny new conda-forge staged recipe review presentation to share: https://travishathaway.github.io/conda-forge-staged-recipe-presentation
  - [ ] https://github.com/travishathaway/conda-forge-staged-recipe-presentation

## From previous meetings

- [ ] ...

## New agenda items

- [x] DJC: `cuda-arch`/`__cuda_arch` support update
    - cuDNN is the first live package to depend on `cuda-arch`
        - https://github.com/conda-forge/cudnn-feedstock/pull/150
    - `cuda-arch` will "infect" the dependency tree
        - https://github.com/conda-incubator/nvidia-virtual-packages/issues/40
- [x] WV: AMD GPU support merged in rattler
    - [x] Also virtual package plugin CEPs are ready to be looked at 
- [x] WV: swift-compiler recipe (https://github.com/conda-forge/staged-recipes/pull/34391)
- [x] WV: conda OCI mirror things are on track again

## Deferred to next meeting

- [ ] ...
