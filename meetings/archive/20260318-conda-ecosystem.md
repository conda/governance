---
tags: [meeting-notes]
---
# 2026-03-18 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

1. JRG: Jaime Rodríguez-Guerra (@jaimergp), Quansight, C/SC, CF/C.
2. BZ: Bas Zalmstra (@baszalmstra), Prefix.dev, C/SC, CF/C
3. TH: Travis Hathaway (@travishathaway), Anaconda
4. RA: Ruben Arts (@ruben-arts), Prefix.dev
5. CHL: Cheng H. Lee (@chenghlee), Anaconda, C/SC, CF/C
6. SC: Sophia Castellarin (@soapy1), Openteams
7. SM: Schuyler Martin (@schuylermartin45), Anaconda
8. LW: Lilly Winfree (@lwinfree), Anaconda
9. BM: Ben Moss (@benmoss), Bloomberg
10. JK: John Kirkham (@jakirkham), NVIDIA, C/SC, CF/C

## Announcements

- [x] JRG: conda-forge/core, ongoing vote to add Pavel to staged-recipes. Check Zulip/core, email o go to https://vote.heliosvoting.org and log in with Github.
- [X] JRG: conda/steering-council, RFC periods open for:
    - Multi-output cache in recipe.yaml: https://github.com/conda/ceps/pull/102
    - Backwards compatible repodata update strategies: https://github.com/conda/ceps/pull/146
    - BZ: Will open Channel relations in repodata CEP for RFC this week. https://github.com/conda/ceps/pull/155

## From previous meetings

- [X] JRG: Low attendance in the last few 2PM UTC meetings. Maybe time to reconsider whether this timeslot fits its intended purpose. What about an earlier time to cater to APAC a bit better? 9am UTC? Probably need to run a survey.
    - Run survey in both zulips
    - JRG: Reminder: source of truth for the calendar invites is at https://conda.org/community/calendar. Delete existing ones and add those instead.

## New agenda items

- [X] JRG: conda-forge: Upcoming Github Actions rollout for Linux. Check https://github.com/conda-forge/conda-forge.github.io/issues/2771 for details.
    - Need to unify some configuration options in conda-smithy: feedback needed at https://github.com/conda-forge/conda-smithy/issues/2349
- [X] TH: Conda Support/Issue Triaging Meetings (maybe conda-forge help too?)
    - Community meeting specifically targeted towards new contributors or people looking for support
    - Build it, and they will come? Will people actually show up? How to conduct outreach?
    - [X] JRG xref: "open office hours" https://github.com/conda/governance/issues/113
- [X] TH: Sovereign Tech Fund Scholarships
    - [X] https://www.sovereign.tech/news/2026-fellowship-applications-open
    - [x] Should we apply? Does conda-forge stand to benefit for extra paid help?
    - [x] LW: Reminder, not just code maintenance: "We are expanding the fellowship program beyond FOSS maintainers to also include community managers and technical writers, and we will contract up to 12 Sovereign Tech Fellows." -> Hiring a community manager?
    - [x] JRG: Action items: share with steering-council, core team to see if any existing members may want to apply.
