# 2022-06-08 Conda Community Meeting

* [Meeting link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/UTC/2022-06-08/17:00/b/Conda%20community%20meeting)

## Attendees

| Name                     | Initials | Affiliation   | GH Username        |
| -------------------------| -------- | ------------- | ------------------ |
| Cheng H. Lee             | CHL      | Anaconda      | chenghlee          |
| Jannis Leidel            | JL       | Anaconda      | jezdez             |
| Jaime Rodríguez-G.       | JRG      | Quansight/cf  | jaimergp           |
| Dave Clements            | DPC      | Anaconda      | tnabtaf            |
| Carl Anderson            | CA       | Anaconda      | barabo             |
| Daniel J. Ching          | DJC      | Argonne       | carterbox          |
| Katherine Kinnaman       | KK       | Anaconda      | kathatherine       |
| Matthew R Becker         | MRB      | cf            | beckermr           |
| Sebastien Awwad          | SA       | Anaconda      | awwad              |
| Bianca Henderson         | BH       | Anaconda      | beeankha           |
| John Kirkham             | JK       | NVIDIA/cf     | jakirkham          |
| Travis Hathaway          | TH       | Anaconda      | travishathaway     |
| Daniel Holth             | DH       | Anaconda      | dholth             |
| Marcelo Trevisani        | MDT      | conda-forge   | marcelotrevisani   |
| Mike McCarty             | MM       | NVIDIA        | mmccarty           |

19 people present


## Introductions


## Announcements

* [x] Vote on CEP 6 (channel notifications) started today!
    * [ ] Steering council members, please vote: https://github.com/conda-incubator/ceps/pull/19#issuecomment-1150096980
    * Corresponding PR: https://github.com/conda/conda/pull/11462


## New Agenda Items

* [x] (DPC) Governance update
  * Code of Conduct PR will be submitted to Steering Council tomorrow.  Current draft is [here](https://github.com/tnabtaf/governance/blob/code-of-conduct/CODE_OF_CONDUCT.md).
  * Will start applying [policies described here](https://github.com/conda-incubator/governance/issues/47) to [Governance](https://github.com/conda-incubator/governance/blob/master/README.md) this week.  Look for a PR in a week or so.
  * Will also draft a NumFOCUS Fiscal Sponsorship application in next two weeks. Aiming for review in July.

* [x] (CA;DH) conda-incubator/conda-index performance update
    * ![It's so beautiful!](https://i.imgur.com/bJctloB.png)
    * Can now clone conda-forge in ~8 minutes on avg; release to prod this week.
    * conda-index now backed by SQLite.
    * Anaconda preparing to open-source code used to clone channels.
    * By end of next week, should be released to all cloned channels (bioconda, pytorch, etc.)
    * Will begin publishing `repodata.jlap` and `current_repodata.jlap` (differences beteween successive `repodata.json`) as an experiment. *does not appear in index.html*

* [x] (CHL) Windows on ARM support
    * https://github.com/conda/conda/issues/11472
    * Anaconda starting discussions with Linaro on getting this moving
    * Expect conda/conda-build PRs to enable `win-arm64` as a supported platform 
    * CHL will make introductions to c-f core team.

* [x] (JL) conda 4.13.0/conda-build 3.21.8|9 release incident
    * Incident report: https://hackmd.io/nD5UzWJVQ2mPzYnvQyGqMA?view
    * Various CEPs in draft to improve the situation

* [x] (JRG) conda-standalone & constructor development
    * How should we support these projects as a community?
    * Constructor: want to merge various forks back into main project
        * Napari fork: https://napari.org/developers/packaging.html#constructor-based-installers
        * Anaconda fork currently private; working on-going to upstream differences
        * (JL) Formally ask Steering Council to formally create a constructor project team; general consensus is that we should do this.
        * Continue conversation here: https://github.com/conda/constructor/issues/497
    * (JL) Get Anaconda and c-f conda-standalone recipes to converge

* [x] (MRB) status of anaconda.org support for sha256 and .conda
    * .conda support ready to be released within next week or so.
    * SHA-256 in beta test; initial release will not backfill checksums but will generate SHA-256s for newly uploaded packages.
    * Will the anaconda.org API return SHA-256 for packages? (It should, but SC will check and confirm.)


## What is this meeting for?

Various parts of the conda community gather on a regular basis.  This meeting brings together all of these sub-communities for a community wide call.