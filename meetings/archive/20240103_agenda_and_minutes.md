---
tags: [meeting-notes]
---
# 2024-01-03 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Bas Zalmstra           | BZ       | Prefix.dev   | baszalmstra      |
| Jaime Rodríguez-Guerra | JRG      | Quansight    | jaimergp         |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Dave Clements          | DPC      | Anaconda     | tnabtaf          |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Wolf Vollprecht        | WV       | Prefix.dev   | wolfv            |
|                        |          |              |                  |

8 people in total

## Introductions

- [ ]

## Announcements

- [ ]

## New Agenda Items

- [x] JRG: I added a ['latest updates' view to conda-metadata](https://conda-metadata-app.streamlit.app/?q=conda-forge). But... [bioconda RSS.xml is broken](https://conda.anaconda.org/bioconda/rss.xml)? 
    - CL: Bioconda is using an older version of conda-index in the CDN.
    - JRG: will report this in the infra repo.
- [x] DPC: Handoffs
    - Mastodon, Buffer, LinkedIn, condamanager@gmail.com, ...
    - JL: NumFOCUS has google workspace. We need to set that up.
    - JL: Dave please write up what you got done, and what you didn't.
        - Probably do this in HackMD.
    - JL: Governance?
        - Two person rule, funding, 
        - DPC: If I get to this it will be in a fork/PR, but will not be submitted for voting.
- [x] WV: recipe format
    - still working through some changes. E.g. added `pip_check` to `python` test with `default: true`
    - Planning to have vote, but more changes are coming up.
    - Multiple tests.
    - torn between calling for a vote, and waiting for more changes.
    - JL: Suggest voting as soon as possible, because minor changes to a CEP later is not a big effort.  CAn help with mechanics of vote.
    - WV/JL will meet tomorrow to get this mmoving.
- [x] WV: Rattler build implementing overlinking and underlinking checks.
- [x] JL: Year of build tools! 
    - conda-build goes to calver
        - deprecations galore
    - improve automation of package building.
    - Want a meeting this month about build tools and long term planning.
        - new recipe format
        - reference implementation in Rattler-build
- [x] JL: Plugin hooks for Rust
    - WV: this can be done

- [ ] JL: Future of Mamba?
    - https://github.com/mamba-org/mamba/pull/3054 


