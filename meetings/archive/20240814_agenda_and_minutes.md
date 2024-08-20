---
tags: [meeting-notes]
---
# 2024-08-14 Conda Community Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Schuyler Martin        | SM       | Anaconda     | schuylermartin45 |
| Filipe Fernandes       | FF       | conda-forge  | ocefpaf          |
| Eric Dill              | ED       | Anaconda/CF  | ericdill         |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Marco Esters           | ME       | Anaconda     | marcoesters      |
| Jaime Rodríguez-Guerra | JRG      | Quansight    | jaimergp         |
| Cheng H. Lee           | CHL      | Anaconda/CF  | chenghlee        |
| Aaron Opfer            | AO       |              |                  |
| Daniel Holth           | DH       | Anaconda     | dholth           |
| Dasha Gurova           | DG       | Anaconda     | dashagurova      |

X people in total

## Introductions

- [ ]

## Announcements

- [ ]

## New Agenda Items

- [ ] (DG)Conda Communications update:
    - conda ecosystem explained blog PR: https://github.com/conda-incubator/conda-dot-org/pull/198
        - preview: https://deploy-preview-198--conda-dot-org.netlify.app/blog/2024-08-14-conda-ecosystem-explained
    - New YouTube channel too
    - Twitter? Mastodon?
    - AO: "-c conda-forge" instructions in projects documentation for a Miniconda install will make you mix defaults and conda-forge. We are not documenting this well, or even enforcing this in the conda clients.
        - JRG: Draft a cep that proposes a convention for channels to have "_abi_tag" packages that export a fingerprint they commit to. e.g. conda-forge and bioconda would both have `_abi_tag=2024.8.14=conda-forge`, defaults would have `_abi_tag=2024.8.14=defaults`. If this doesn't work, maybe some repodata.json fields.
- AO: Demo about `conda-curation`: https://github.com/AaronOpfer/conda_curation
    - AO: Written in Rust, purpose to filter out unneeded things from repodata.json
        - Performance improvements for the downstream solves, better error messages
    - JRG: Similar to https://github.com/conda-incubator/conda-subchannel?
    - 
