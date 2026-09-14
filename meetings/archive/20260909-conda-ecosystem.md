---
tags: [meeting-notes]
---
# 2026-09-09 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

<!-- Use this syntax:
* Initials: Full Name (@github-username), Affiliation.
* SD: Sam Doe (@samdoe), Company
-->

1. TH: Travis Hathaway (@travishathaway), Anaconda
1. DY: Dan Yeaw (@danyeaw), Anaconda
1. DJC: Daniel Ching (@carterbox), CF/C, NVIDIA
1. LH: Ludovic Henry (@luhenry), Qualcomm/RISE (RISC-V)
1. PZ: Pavel Zwerschke (@pavelzw), QuantCo, C/SC
1. BZ: Bas Zalmstra (@baszalmstra), Prefix.dev, C/SC, CF/C
3. WV: Wolf Vollprecht (@wolfv), Prefix.dev, C/SC, CF/C

<!-- Delete sections that do not apply before committing to repo -->
<!-- Every agenda item must use the initials of the person adding the item -->


## Introductions

- [ ] ...

## Announcements

<!-- New releases, upcoming changes, ongoing votes --->

- [x] Welcome Daniel Ching to conda-forge/core!
- [ ] Open votes:
    - [ ] 2026-09-21: conda-forge/core, new member nomination at https://vote.heliosvoting.org
    - [ ] 2026-09-16: conda/steering-council, CEP at https://github.com/conda/ceps/pull/159
- [ ] Python Packaging Council vote is ongoing too
    - Might be too late to join PSF if you're not already a member though :grimacing:

## From previous meetings

- [ ] ...

## New agenda items

- [x] (DJC) Close CUDA 13.0 Migration
    - [x] Remove opt-in 11.8 Migrator
    - [x] https://github.com/conda-forge/conda-forge-pinning-feedstock/pull/8562
- [x] (DJC) Open CUDA 13.4 Migration
    - [x] https://github.com/conda-forge/conda-forge-pinning-feedstock/pull/8926
    - [x] IF: We don't need a migration we can just update the global pinnings after 13.0 migration end
- [x] (DJC) Add nvidia-virtual-packages to either conda-forge-ci-setup or conda dependencies
    - [ ] Support for `__cuda_arch` is blocked for v0 recipes until nvidia-virtual-packages is available in the CI environment 
    - [ ] https://github.com/conda-forge/conda-forge-ci-setup-feedstock/pull/427
    - [ ] https://github.com/conda-forge/conda-feedstock/pull/315
    - [ ] WV: What is the performance cost of virtual package detection?
        - [ ] TH: Offering to do some benchmarking
            - [ ] TH: Doesn't actually have a GPU, so this may make things difficult :joy: 
    - [ ] IF: Please post benchmarks in the PR on conda-feedstock
    - [ ] WV: Could instead add a dependency to conda-build?
- [x] (TH) Presenting about staged recipe contribution at the end of the month at https://meetup.doepy.org/
    - [x] What are some resources talking about the history of conda-forge? (just conda-forge.org)
        - [x] Reach out to people via DMs
    - [x] See: https://conda-forge.zulipchat.com/#narrow/channel/520881-staged-recipes/topic/Getting.20involved.20in.20staged-recipes.20reviews/with/622166039
        - [x] I'm curious about how I should go about recruiting new reviewers. I know there's a currently a need for more c/cpp reviewers. Are there other deficits I need to know about?
    - [x] Should I have someone from conda-forge core review my slides beforehand? Or do I have everyone's blessing :pray:
- [x] (LH) Native runners for RISC-V in conda-forge
    - Miniforge has a release on linux-riscv64: https://github.com/conda-forge/miniforge/releases/tag/26.7.2-0
    - Validating it [works in llvmlite/numba](https://github.com/numba/llvmlite/pull/1485)
    - Missing [conda-incubator/setup-miniconda](https://github.com/conda-incubator/setup-miniconda/pull/567)
    - Still missing docker image, and `conda-forge-ci-setup`
        - Miniforge testing is disabled because missing docker image
    - Native runners?
        - [RISE RISC-V Runners](https://github.com/apps/rise-risc-v-runners); backed by RISE (Linux Foundation project), OSS, free to use, native GitHub integration, used by other projects (CNCF, PyTorch, Llama.cpp, Numpy, ...), not RVA23; Contact: @luhenry
        - OpenEuler, based on OpenStack, would need GitHub integration
- [x] (WV) Vote opening on sigstore serving CEP proposoal
    - [ ] {%preview https://github.com/conda/ceps/pull/142 %}
- [x] (IF) rattler-build v1 recipes not running tests under cross compilation + user space emulation
    - [ ] https://github.com/prefix-dev/rattler-build/issues/2587

## Deferred to next meeting

- [ ] ...
