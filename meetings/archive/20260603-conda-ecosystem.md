---
tags: [meeting-notes]
---
# 2026-06-03 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

<!-- Use this syntax:
* Initials: Full Name (@github-username), Affiliation.
* SD: Sam Doe (@samdoe), Company
-->

1. JRG: Jaime Rodríguez-Guerra (@jaimergp), Quansight, C/SC, CF/C
2. TH: Travis Hathaway (@travishathaway), Anaconda
3. JS: Jakov Smolic (@jsmolic), Quansight
4. PZ: Pavel Zwerschke (@pavelzw), QuantCo, C/SC
5. DJC: Daniel Ching (@carterbox), NVIDIA, CF/SR
6. TDJ: Tim de Jager (@tdejager), Prefix.dev
6. WBZ: Bas Zalmstra (@baszalmstra), Prefix.dev, C/SC, CF/C
7. DY: Dan Yeaw (@danyeaw), Anaconda
8. JL: Jannis Leidel (@jezdez), Anaconda, C/SC, CF/C

<!-- Delete sections that do not apply before committing to repo -->
<!-- Every agenda item must use the initials of the person adding the item -->


## Introductions

- [x] Tim from prefix.dev

## New agenda items

- [x] JRG: [CEP 18 amendment request](https://github.com/conda/ceps/issues/150#issuecomment-4603578127).
    - JL: If it's just a patch and doesn't change the intent, it's ok to patch in same CEP.
    - JRG: Implementation of fix breaks backwards compatibility, so leaning towards minting a new CEP number just to be able to refer to the fixed version inequivocally
- [x] DJC: ETA for WOA (Windows on Arm) generally available to conda-forge?
     - https://github.com/conda-forge/conda-forge.github.io/issues/1940
     - NVIDIA wants to sync with release CUDA WOA packages
     - JRG: Sometime this year is realistic
     - WOA rollout depends on GHA Runners rollout
     - JL: We should have physical test machines for smoke tests
- [x] DJC: Can NVIDIA opt-into GHA Runners for feedstocks early?
    - https://github.com/conda-forge/conda-forge.github.io/issues/2771
    - WOA not working, but can already opt-in to GHA except for osx
        - JRG: Planning to enable win-64 on GHA by default in the coming weeks (depends on https://github.com/conda-forge/conda-smithy/issues/2349)
- [x] DY: conda-pypi platypus logo
    - [x] https://github.com/conda/conda-pypi/issues/378
    - [x] Team aligned with us using the likeness of CF/C on the logo
- [x] TH: Possibility to present on how to submit recipes to conda-forge https://meetup.doepy.org/
    - [x] Would be nice a opportunity to publicize conda-forge more
    - [x] Chance to recruit more review volunteers?
    - [x] More motivation to better document the current review submission process
    - [x] Demo my new [fancy-pants reviewer dashboard](https://srdb.thath.net/) :stuck_out_tongue: (having this presentation could give me a nice deadline to keep my work concentrated)
    - [x] Consensus was that this would be a good idea :white_check_mark: 
- [x] TDJ: Small CVE mapping and purl demo
      URL: https://prefix-dev.github.io/purl-associator/cve.html
      

