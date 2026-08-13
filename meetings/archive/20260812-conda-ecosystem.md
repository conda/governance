---
tags: [meeting-notes]
---
# 2026-08-12 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees


1. JRG: Jaime Rodríguez-Guerra (@jaimergp), Quansight, CF/C, C/SC
1. CHL: Cheng H. Lee (@chenghlee), Anaconda, C/SC, CF/C
1. WV: Wolf Vollprecht (@wolfv), prefix.dev, C/SC, CF/C
1. IF: Isuru Fernando (@isuruf), OpenTeams, C/SC
1. DJC: Daniel Ching (@carterbox), NVIDIA

## Announcements

<!-- New releases, upcoming changes, ongoing votes --->

- [X] Ongoing votes/RFCs:
    - Repodata v3 CEP vote:  https://github.com/conda/ceps/pull/146
    - PURL spec amendment RFC: https://github.com/conda/ceps/pull/159
    - conda-forge/staged-recipes member: check Helios
    - conda-forge/core member: check Helios

## New agenda items

- [X] WV: We are preparing a CEP for virtual package plugins, currently on HackMD, soon on Github: https://hackmd.io/Rwig0llBQiunHx2l2qISxQ
    - IF/DJC: Questions about security concerns and user-channel contracts. Differences with concerns in post-link scripts? Pixi already prevents those from being executed.
    - JRG: Discovery is useful (mapping of virtual packages to their providers), and an interface of the returned values too. No need to couple this to automated installation and arbitrary execution, that's for the client UX to decide. e.g. the same metadata can be used to simply tell the user what they need to do on their own, or how to override manually.
    - JRG: Motivation for more virtual packages now? Thought this had plateaud already.
        - WV: Client with interest in several accelerators, needs a federated mechanism
    - _Conversation was cut short because WV had to hop onto another call. To be continued._

## Deferred to next meeting

- [ ] Continue talking about [virtual packages proposal](https://hackmd.io/Rwig0llBQiunHx2l2qISxQ)
