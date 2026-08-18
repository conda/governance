---
tags: [meeting-notes]
---
# 2026-04-22 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

<!-- Use this syntax:
* Initials: Full Name (@github-username), Affiliation.
* SD: Sam Doe (@samdoe), Company
-->

1. DY: Dan Yeaw (@danyeaw), Anaconda
1. TH: Travis Hathaway (@travishathaway), Anaconda
1. WV: Wolf Vollpecht (@wolfv), C/SC, CF/C, Prefix.dev
1. BZ: Bas Zalmstra (@baszalmstra), C/SC, CF/C, Prefix.dev
1. JRG: Jaime Rodríguez-Guerra (@jaimergp), C/SC, CF/C, Quansight
1. CHL: Cheng H. Lee (@chenghlee), C/SC, CF/C, Anaconda
1. DJC: Daniel Ching (@carterbox), NVIDIA, CF
1. PZ: Pavel Zwerschke (@pavelzw), QuantCo, C/SC
1. JL: Jannis Leidel (@jezdez), Anaconda, CF/C, C/SC

<!-- Delete sections that do not apply before committing to repo -->
<!-- Every agenda item must use the initials of the person adding the item -->


## Introductions

- [ ] ...

## Announcements

<!-- New releases, upcoming changes, ongoing votes --->

- [x] WV: rattler-build 0.63 released with staging output support (what recipe will be first adopter?!)
- [X] BZ: Channel relations CEP 42 landed!
    - No implementations yet, but we will start soon with the clients.
- [x] JRG: Recently approved or minted CEPs ^, plus 39, 40 and 41! (rattler-build CEPs)
- [X] JRG: Ongoing votes/RFCs:
    - conda-forge/core, please check Helios
    - RFC [The __cuda_arch virtual package](https://github.com/conda/ceps/pull/157)
    - [Conditional dependencies, extras, flags](https://github.com/conda/ceps/pull/111)

## New agenda items

- [X] (WV) Ideating around Conda-Forge Security SIG
    - CVEs increasingly popular and important
    - Get funding through NumFOCUS from stakeholders
    - (JL) Should formalize this as a sub-team under the remit of the conda SC?
        - Eventually, yes, but maybe not needed to start working on #1 below.
    - Goal #1: Provide a CVE Mapping
        - (CHL/JL) GH DependaBot team might be interested in consuming that data
        - (CHL) Are we proposing becoming a CNA? If so, for what channels/scope and how do we sustain it?
        - (JRG) First: PURLs for sources and packages? Several CEP drafts. We should finish one of these to get which data we will pull:
            - https://github.com/conda/ceps/pull/63
            - https://github.com/conda/ceps/pull/114
            - https://github.com/conda/ceps/pull/159
    - Action item: create issue in conda/governance to request new repo in conda-incubator (`sig-cve-initiative`?)
- [x] (CHL) Draft CEP for conda package URLs: https://github.com/conda/ceps/pull/159
    - Might be useful for SBOMs and vulnerability (CVE) reporting
    - Still looking over [ECMA 427](https://ecma-international.org/publications-and-standards/standards/ecma-427/), so not quite ready to start formal RFC period
- [x] (JL) Draft CEP for Index timestamp (e.g. for dependency cooldowns)
    - https://github.com/conda/ceps/pull/154
    - Ready for RFC phase based on feedback from prefix.dev and Anaconda staff
    - Future section included for Sigstore adjacent improvements (thanks Wolf!)
    - RFC to start today.
- [X] (JL) Let's make graduating projects easier
    - https://github.com/conda/governance/pull/374
- [x] WV: Welcoming Lucas to Pixi maintainers! 2nd non-Prefix person to join.
- [x] WV: Conversation with Mise maintainers to improve their conda support. Also interested with sigstore, so more eyeballs on the matter, yay!


## Deferred to next meeting

- [ ] ...
