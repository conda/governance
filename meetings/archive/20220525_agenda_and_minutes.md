# 2022-05-25 Conda Community Meeting

* [Meeting link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/UTC/2022-05-25/17:00/b/Conda%20community%20meeting)
* Last week's minutes: https://hackmd.io/24eIfuGpQtOfYmapF-94hw


## Attendees

| Name                     | Initials | Affiliation   | GH Username        |
| -------------------      | -------- | ------------- | ------------------ |
| Daniel Holth             | DH       | Anaconda      | dholth             |
| Ken Odegard              | KO       | Anaconda      | kenodegard         |
| Jannis Leidel            | JL       | Anaconda      | jezdez             |
| Cheng H. Lee             | CHL      | Anaconda      | chenghlee          |
| Bianca Henderson         | BH       | Anaconda      | beeankha           |
| Katherine Kinnaman       | KK       | Anaconda      | kathatherine       |
| Filipe Fernandes         | FF       | conda-forge   | ocefpaf            |
| Jaime Rodríguez-G.       | JRG      | quansight/cf  | jaimergp           |
| Mike McCarty             | MM       | NVIDIA        | mmccarty           |
| John Kirkham             | JK       | cf/NVIDIA     | jakirkham          |
| Mahe Iram Khan           | MIK      | Anaconda      | forgottenprogramme |
| Wolf Vollprecht          | WV       | QuantStack    | wolfv |



## Introductions


## Announcements

- [x] (DH) [Standalone conda-incubator/conda-index with improved performance](https://github.com/conda-incubator/conda-index)
    - (JRG) Any new dependencies? `zstd`, `itertools`, etc.; removes `cph`. DH: adds `zstandard` binding, drops compatibility with Python < 3.9
    - (JRG) Should we have community policy for adding dependencies to core conda projects?
    - (DH) Does anyone use channeldata.json, personally index a lot of conda packages, or need progress bars / user interface on conda-index?
    - (DH) Could complicate indexing during conda-build https://github.com/conda/conda-build/blob/master/conda_build/index.py#L115

- [x] (JL) Calling for vote on CEP 6 - Add Channel Notices to conda
    * Rendered: https://github.com/conda-incubator/ceps/blob/cep-6-channel-notification-feature/cep-6.md
    * Pull request: https://github.com/conda-incubator/ceps/pull/19
    * Implementation (MVP): https://github.com/conda/conda/pull/11462

- [x] (JL) conda 4.13.0 tagged!
    - Release notes: https://github.com/conda/conda/releases/tag/4.13.0
    - Drops support for Python 3.6 and removes a lot of deprecated code (including Python 2.7 support)
    - 7 new contributors!

- [x] (JL) CEPs votes over
    - [x] Vote passed: https://github.com/conda-incubator/ceps/issues/23
    - [x] Vote passed: https://github.com/conda-incubator/ceps/pull/2#issuecomment-1128611445
    - [x] Updates to the CEPs to follow to finalize resolution

## Standing Items


## New Agenda Items

- [x] (KO) Draft [CEP for conda Release Schedule](https://github.com/conda-incubator/ceps/pull/26). Will define future version scheme and release cadence. Need community input.

- [x] (JL) Talks submissions or attendence for EuroSciPy 2022 this year? Basel, Switzerland from Aug 29 to Sept 2.

- [x] (JL) conda summit: Current waiting on feedback from SciPy 2022 regarding development sprint application
    - (CHL) Should have accept/decline notice from SciPy organizers in next week or two (early June)
    - Join planning discussion in #conda-summit channel in conda Slack channel

- [ ] (DPC) [Governance proposal](https://github.com/conda-incubator/governance/issues/47).
    - Goals
        - Preserve most of the current proposed governance model in conda-incubator. This is based on conda-forge’s governance model.
        - Encourage community and commercial / organizational involvement and innovation.
        - Prevent capture of the conda organization by any one funding organization.
        - Assure the conda community that Anaconda and other commercial entities are truly limited in what they can do going forward.
        - Make the Conda Organization a fiscally-sponsored project, most likely with NumFOCUS.
    - Highlights
        - Pay attention to steering council member funding.
            - Limit # of voting members based on shared funding.
        - Encourage early Provisional membership for organizations that fund conda ecosystem work.


## What is this meeting for?

Various parts of the conda community gather on a regular basis.  This meeting brings together all of these sub-communities for a community wide call.
