---
tags: [meeting-notes]
---
# 2026-09-23 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

<!-- Use this syntax:
* Initials: Full Name (@github-username), Affiliation.
* SD: Sam Doe (@samdoe), Company
-->

1. JRG: Jaime Rodríguez-Guerra (@jaimergp), Quansight
2. LH: Ludovic Henry (@luhenry), RISE/Qualcomm
3. TH: Travis Hathaway (@travishathaway), Anaconda
4. PZ: Pavel Zwerschke (@pavelzw), QuantCo
5. IF: Isuru Fernando (@isuruf), OpenTeams
6. NB: Nick Bollweg (@bollwyvl)
7. WV: Wolf Vollprecht (@wolfv), Prefix

## Introductions

- [x] Ludovic from RISE/Qualcomm, helping with RISC-V

## Announcements

- [x] (JRG) SC approved [conda PURL CEP](https://github.com/conda/ceps/pull/159) as CEP 49, and [SigStore attestations serving CEP](https://github.com/conda/ceps/pull/142) as CEP 50

## New agenda items

- [x] (TH) Demo of "[Feedstock Maintainers](https://travishathaway.github.io/feedstock-maintainers/)" and share my ideas about a development roadmap :world_map: 
    - Python CLI that does the scraping, plus a webapp that presents the data
    - Implemented as a set of GHA workflows + a static webapp
    - Shows maintainer statistics since inception
    - Overview of each maintainer and their work on conda-forge
    - Also some per-package statistics, highlighting maintenance risks
    - Shoutout to [Linux Foundation Insights](https://insights.linuxfoundation.org)
    - Interest in contributing this to conda-forge.org once incubated
        - JRG: Make sure backend/frontend setup is compatible with the website (bunch of regenerated JSON payloads loaded by a React component on Docusaurus)
- [x] (LH) RISC-V VMs being setup. Will reach out once ready.
- [x] (JRG) NSIS for win-arm64? Repackage win-32 as well?
    - IF: Make it noarch:generic with `__win`

