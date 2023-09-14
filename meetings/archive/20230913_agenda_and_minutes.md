---
tags: [meeting-notes]
---
# 2023-09-13 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Maurice Meyer          | MM       | Anaconda     | morremeyer       |
| Daniel Holth           | DH       | Anaconda     | dholth           |
| Bianca Henderson       | BH       | Anaconda     | beeankha         |
| Travis Hathaway        | TH       | Anaconda     | travishathaway   |
| Bas Zalmstra           | BZ       | Prefix.dev   | baszalmstra
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp 

X people in total

## Introductions

- Maurice

## Announcements

- [x] DH: [conda-index to switch to compact output by default](https://github.com/conda/conda-index/pull/112) (conda-forge, defaults repodata.json as a single line of text, not pretty-printed). No deployment timeline yet.
- [ ] DH: [CEP 12 run_exports.json merged into conda-index](https://github.com/conda/conda-index/pull/110)
- [x] BH: Conda [23.7.4](https://github.com/conda/conda/releases/tag/23.7.4) is on defaults

## New Agenda Items

- [x] DH: [CEP to add base_url to repodata.json](https://github.com/conda-incubator/ceps/pull/61) making it possible to serve repodata.json and packages from separate directories.
- [x] MM: Continue work on standardizing schemas
    - Schemas in https://github.com/conda/schemas
        - JRG: See https://github.com/conda/schemas/pull/26 for some unfinished yet more updated work
        - BZ: We implemented very strict schema in rattler. Would be nice to standardize (e.g. JRGs work).
    - I'd like to move them from Draft to adopted as standard
- [x] JRG: Feedback from the NumFOCUS summit: start "conda(-forge)" office hours
  - [x] The idea is to have a space for newcomers and users alike to have questions, solve doubts or seek advice from experts in the community. It could run one hour before the biweekly call. The biweekly is a bit decision oriented and could be daunting for novices so that's the idea. Jaime will try it for a bit, but there were more ideas (casting/streaming the session, chat rooms, etc).
