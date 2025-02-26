---
tags: [meeting-notes]
---
# 2025-02-26 Conda Community Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Jonathan Helmus        |  JJH     | Anaconda     | jjhelmus         |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| John Kirkham           | JK       | NVIDIA/cf    | jakirkham        |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |

X people in total

## Introductions

- [ ]

## Announcements

- [ ]

## New Agenda Items

- [x] (JK) Python 3.13
    - https://github.com/conda/conda/issues/14554
    - https://github.com/conda/conda-build/issues/5625
- [x] Conda Windows Launcher ARM
    - Lots of past discussion
        - https://github.com/conda/conda-launchers/issues/5
        - https://github.com/conda/conda/pull/14401
    - Summarizing signing discussion
        - (JK) IIUC Anaconda wants to build and ship its own binaries, but has yet to do this for ARM
        - (JK) Community wants to add ARM and has done hard work, but can't publish binaries
        - How can both parties get what they want?
    - Proposals
        - Anaconda builds and signs binaries adds them to Conda
        - Public CI pipeline added to build and publish binaries (who signs these? NF?)
        - Build packages in conda-forge & AnacondaRecipes, signed by the respective distributions/sponsors
        - Depending on what is chosen above, do we want to maintain conda-launchers in a separate repo?
            - Or should it be absorbed into conda?
            - Or should it be converted into a feedstock?
    - Follow ups:
        - conda-forge to build own `conda-launcher`, signed using certificate provided by NumFOCUS
        - Anaconda to build separate `conda-launcher`, signed using their internal certificate
        - Call on steering council to graduate conda-launcher
        - PR to conda to remove launchers from src and add dependency on conda-launcher
        - Update conda-forge conda-feedstock to use `conda-launcher` signed binaries
        - Document process and learnings so the broader community can benefit
- [x] (PZ) S3 support in rattler :tada:
- [x] JS bindings to rattler
- [x] CEPS:
    - [run_exports in sharded repodata](https://github.com/conda/ceps/pull/108) 
        - changed to use `patch_instructions_version: 2` for patch instructions 
        - (JL) We should open a `conda-index` ticket to add support for above
        - (WV) would like to move this CEP for a vote ASAP
    - [cache key in rattler-build](https://github.com/conda/ceps/pull/102)
        - [ ] would like to go with an explicit `attach_run_exports_to: [ output name ]`
        - [ ] https://github.com/conda/ceps/pull/102
    - [repodata v2](https://github.com/conda/ceps/pull/111)
    - [sigstore predicate](https://github.com/conda/ceps/pull/112)
- [ ] Conda participation in GSOC
    - [ ] https://github.com/conda/rattler/issues/1058
- [ ] Shell completions with pixi & rattler
    - [ ] Rattler: https://github.com/conda/rattler/pull/1075
    - [ ] Pixi: https://github.com/prefix-dev/pixi/pull/3219