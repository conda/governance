---
tags: [meeting-notes]
---
# 2023-09-27 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Daniel Holth           | DH       | Anaconda     | dholth           |
| Jannis Leidel          | JL       | Anaconda/cf  | jezdez           |
| Ken Odegard            | KO       | Anaconda     | kenodegard       |
| Sebastien Awwad        | SA       |              | awwad            |
| Maurice Meyer          | MM       | Anaconda     | morremeyer       |
| Wolf Vollprecht        | WV       | prefix.dev   | wolfv            |
| Rachel Asquith         | RAA      | Anaconda     | rasquith         |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Carl Anderson          | CPA      | Anaconda     | barabo           |
| Dave Clemtns           | DPC      | Anaconda     |                  |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp         |
| Bianca Henderson       | BH       | Anaconda     | beeankha         | 

14 people in total

## Introductions

- [ ]

## Announcements

- [x] (JL) September releases are coming!
    - conda ([23.9.0](https://github.com/conda/conda/issues/13080))
    - conda-build ([3.27.0](https://github.com/conda/conda-build/issues/5011))
    - conda-libmamba-solver ([23.9.0](https://github.com/conda/conda-libmamba-solver/issues/277))
    - Jaime, Ken and I are planning to tag the releases this week and likely will release to defaults next week (depending on packaging queue). We’ll keep an eye on the conda-forge feedstock as well, as always.
    - Please don’t hesitate to trial the canaries via:
        - `conda install -c conda-canary/label/rc-conda-23.9.x conda`
        - `conda install -c conda-canary/label/rc-conda-build-3.27.x conda-build` etc.
        - `conda install -c conda-canary/label/dev conda-libmamba-solver ` (relase branch not yet created)
    - **IMPORTANT** (get ready!)
        - [Special announcement about rollout of default solver switch to `libmamba`](https://github.com/conda/conda/blob/11c9a09f1a1a701af9eb03e128499d2281bf948a/CHANGELOG.md#special-announcement) (TLDR; It'll come in an extra special release conda 23.10.0!)
- [x] (DH) [conda-index 0.3.0](https://github.com/conda/conda-index/blob/main/CHANGELOG.md) deployed to defaults, conda-forge.
    - Provide [run_exports.json](https://github.com/conda-incubator/ceps/blob/main/cep-12.md)
    - Compact json on conda-forge reduces uncompressed repodata.json size by 27%
    - CDN outage (we forgot to re-enable the `cron` job.  :grimacing:)
- [x] (MM) Updates on caching for CDN-synced channels on anaconda.org
    - Initial test run was very successful
    - We will migrate CDN-synced channels to the new cache over the upcoming weeks (no format changes!)
    - Other channels will follow later
- [x] (JRG) conda-libmamba-solver 23.9 goodies for the curious:
  - Simpler logic, easier to maintain, closer to mamba while respecting the good parts of conda classic. Details of deviation in the docs: https://conda.github.io/conda-libmamba-solver/libmamba-vs-classic/#intentional-deviations-from-classic
  - Faster repodata loading! (30% or so)
  - No more pin overrides. We closed a [4-digit issue](https://github.com/conda/conda/issues/9016) with that one.
  - Overall, feels faster too. See QA notes: https://hackmd.io/GdQoVv3ZSNCj_na6UBJE2A. Hot caches allow solves in <2s.


## New Agenda Items

- [x] (KO) release tooling ([rever](https://github.com/regro/rever)) is no longer actively maintained
    - last released 2 years ago
    - effort to revive a year ago [fizzled out](https://github.com/regro/rever/issues/258)
    - should we be focusing on using alternative tools (e.g. [cranko](https://pkgw.github.io/cranko/book/latest/))?
    - will bring this up next week at conda-forge community meeting
    - JRG: conda-smithy release via rever but I'd say the team would be happy to change to something simpler too. A good policy on PR titles would go a long way towards simplification.
- [x] (DH) Possible for jlap CEP to get a vote?