---
tags: [meeting-notes]
---
# 2023-11-08 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
|  Dave Clements         | DPC      | Anaconda     | tnabtaf          |
| Jaime Rodríguez-Guerra | JRG      | Quansight    | jaimergp         |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Marcel Bargull         | MB       | Bioconda/cf  | mbargull         |
| Wolf Vollprecht        | WV       | prefix.dev   | wolfv            |
| Daniel Holth           | DH       | Anaconda     | dholth           |
| Jannis Leidel          | JL       | Anaconda/cf  | jezdez           |
| Ken Odegard            | KO       | Anaconda     | kenodegard       |
|                        |          |              |                  |
|                        |          |              |                  |

10 people in total

## Introductions

- [ ]

## Announcements

- [ ]

## New Agenda Items

- [x] (DPC) [Zenodo](https://zenodo.org/)
    - Want to create a [DOI](https://www.doi.org/the-identifier/what-is-a-doi/) for conda on Zenodo, so the project can be referenced.
    - Bioconda has a real paper, but conda does not.
    - Any reason not to do this?
    - Jannis has created an organization in Zenodo
        - And the latest conda release now has a DOI. Automagically.
        - 
    - GitHub repo of conda itself is citeable, as of a year ago or so.
    - Jaime There are two types
        - Project
        - Sub doi's for each release.
    - Take homes
        - Encourage our sub-projects to create them
        - Look into Organization DOI
- [X] (DPC) Time to get off Twitter?
    - Suggest "retiring" the account, which means not closing it, but no longer posting to it,
    - And then pointing to Mastodon.
    - Should we move Mastodon servers?  Fosstodon is now invite only.
    - Jannis: Create a LinkedIn group?
    - Twitter has become toxic, and less usable every week.
    - Wolf: why not just post stuff because it's easy?
    - Dave: It reflects badly on us to support this.
    - Wolf: "When Google leaves, we leave" speaking about Prefix.
    - Jannis:
        - Create a ticket, summarize what others are doing, and then nominate a candidate solution.
    - Marcel: Lean towards moving slowly here. Would still makes sense to keep posting to Twitter.
    - 
- [x] (DPC) Anything to highlight in November Newsletter?
- [x] (TH) New docs team :rocket:
    - [x] Please sign up if interested to help with documentation related efforts: https://github.com/conda/conda-docs/issues/780 (leave a comment on the issue, and I will add you)
    - [x] First project is the revamp of the conda docs with a new theme (demo)
        - [x] Pull request: https://github.com/conda/conda/pull/13298
    - [x] Also the creation and maintenance of a [conda-sphinx-theme](https:github.com/conda-incubator/conda-sphinx-theme)
- [x] (WV) Ongoing implementation of rattler-build with the new recipe format
    - [ ] CEP for (new) keys & values is open for comments: https://github.com/conda-incubator/ceps/pull/56
    - [ ] Jinja function CEP
    - [ ] Multi-output CEP
    - [ ] Rendered output CEP
    - [ ] Tests section CEP https://github.com/conda-incubator/ceps/pull/57
    - [ ] Also working towards making builds more reproducible
- [x] (JL) conda 23.10.0 happened! For real this time, in November :grimacing: 
    - currently looking good, positive response so far, a few tickets to be fixed in a minor release of conda-libmamba-solver
    - planned to be added in a future miniconda release (no ETA yet IIUC)
    - Issues with redefined defaults & conda-build: https://github.com/conda/conda-libmamba-solver/pull/365
- [ ] (JRG) Provenance info in our package metadata (demo).
  - [ ] See 'provenance' cell in https://conda-metadata-app.streamlit.app/?q=conda-forge%2Fnoarch%2Fmakim-1.8.3-pyh707e725_0.conda
  - [ ] Source at: https://github.com/Quansight-Labs/conda-metadata-app
  - [ ] 'Whatprovides' dataset by Daniel: https://conda-whatprovides.fly.dev/metayaml?sql=select+paths.path%2C+paths_entries.*+from+paths+join+paths_to_entries+on+%28paths.id+%3D+path_id%29+join+paths_entries+on+%28entry_id+%3D+paths_entries.id%29+where+path+%3D+%3Apath&path=main%2Flinux-64%2F_ipyw_jlab_nb_ext_conf-0.1.0-py38h06a4308_1.conda
- [x] Time for this meeting? Should we move it earlier in the day?
    - Nothing decided, not even next steps.
