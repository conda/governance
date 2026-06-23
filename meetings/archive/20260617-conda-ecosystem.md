---
tags: [meeting-notes]
---
# 2026-06-17 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

1. TH: Travis Hathaway (@travishathaway), Anaconda
2. BZ: Bas Zalmstra (@baszalmstra), Prefix.dev, CF/C, C/SC
3. DY: Dan Yeaw (@danyeaw), Anaconda
4. WV: Wolf Vollprecht (@wolfv), Prefix.dev, CF/C, C/SC
5. CHL: Cheng H. Lee (@chenghlee), Anaconda, C/SC, CF/C
6. JL: Jannis Leidel (@jezdez), Anaconda, C/SC, CF/C
7. JRG: Jaime Rodríguez-Guerra (@jaimergp), Quansight, C/SC, CF/C


## Announcements

<!-- New releases, upcoming changes, ongoing votes --->

- [X] @ conda/steering council: CEP vote at https://github.com/conda/ceps/pull/154
- [X] @ conda-forge/core: CFEP vote at https://github.com/conda-forge/cfep/pull/65. Ends today.

## New agenda items

- [X] (BZ) Use of regex in build strings in https://github.com/conda-forge/microarch-level-feedstock/pull/26
- [x] (WV) New release of sigstore-rust
    - Also want to finalize [the `verification` CEP](https://github.com/conda/ceps/pull/168) soon!
    - And integrate verification into the recipe
- [X] (WV) Lots of performance improvements across the board (resolvo improvements on solver side, linking improvements on rattler side). Client releases available soon.
    - https://github.com/sigstore/sigstore-rust
- [x] (TH) Should I continue work adding Python sigstore to conda-forge?
    - [x] https://github.com/conda-forge/staged-recipes/pull/32321
    - [x] JL: Happy to help if there is no interest in this, this is a critical library for the Python ecosystem
    - [x] TH: will revisit my work and see how easy it is to write Python bindings for sigstore-rust

