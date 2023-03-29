---
tags: [meeting-notes]
---
# 2023-03-29 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Filipe Fernandes       | FF       | conda-forge  | ocefpaf          |
| Jannis Leidel          | JL       | conda/cf     | jezdez           |
| Dave Clements          | DPC      | Anaconda     | tnabtaf          |
| Daniel Holth           | DH       | Anaconda     | dholth           |
| Eric Dill              | ED       | Anaconda/cf  | ericdill         |
| Katherine Abrikian     | KCA      | Anaconda     | kalawac          |
| Travis Hathaway        | TH       | Anaconda     | travishathaway   |
| Jesse Wiles            | JWW      | Anaconda     | jessewiles       |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Ken Odegard            | KO       | Anaconda     | kenodegard       |
| Marcelo Trevisani      | MDT      | conda-forge  | marcelotrevisani |
| John Kirkham           | JK       | NVIDIA/cf    | jakirkham        |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp         |
| Sebastien Awwad        | SA       | Anaconda     | awwad            |
| | | | |
| | | | |

18 people in total

## Introductions :wave: 

- [x]

## Announcements :loudspeaker: 

- [x] (DPC) Conferences :house_buildings: 
    - Conda Ecosystem Open Space proposal submitted to PyCon US 2023
    - Conda talk submitted to US RSE 2023, will submit conda-forge tutorial in the next week
    - CHL submitted "conda and friends" sprint proposal to SciPy 2023

- [x] conda-build 3.24.0 released! :tada: 
    - https://github.com/conda/conda-build/releases/tag/3.24.0
    - 6 new contributors!

## New Agenda Items :newspaper: 

- [x] (TH) Conda Version Support CEP: https://github.com/conda-incubator/ceps/pull/25
    - Revised from an earlier attempt
    - Now, we only want to support the most recent version
    - Ready to be discussed and voted on
    - Extension of CEP-8 and -9
    - (JK) How would this impact API that tools like conda-smithy depend on?
        - Changes should follow the published deprecation policy.
        - Need to restart discussion about API: https://github.com/conda/conda/issues/11925
- [x] (CHL) Should we ~~deprecate~~ fix the [conda/schemas](https://github.com/conda/schemas) repo?
    - What CEPs do we need to write?
    - (JL) Should there be a spec/CEP working group to move this forward? 
    - Leaning hard towards fixing the schemas instead of deleting them wholesale
    - Some are only partly implemented.  Some are not.
    - (CHL) happy to lead cleanup.
    - In the meantime, flag them as inaccurate, but also say we are actively working on it.
- [x] (DH) Need feedback on repodata.state.json rename CEP, also adds locking and modifies cache revalidate checks. https://github.com/conda-incubator/ceps/pull/48/files
- [ ] (JL) conda-build release policy
    - part of the larger initiative to ramp up on maintenance: https://github.com/conda/conda-build/issues/4697
    - recent code changes broke conda-forge scripts (`NameError`)
    - ~140 releases of conda-build 3.x!
    - skeleton and index should be going out
    - CEP 8 and 9 look promising for conda, also for conda-build?
    - Draft: conda-build adopts CEP 9 with an accelerated deprecation cycle without pending deprecation and just one regular release between deprecation and removal, resulting in a 2-5 months depreciation window
    - Alternatives:
        - aggressively follow SemVer (e.g. conda-build 4.0 drops skeleton and index)
        - rewrite rather than trying to fix?
        - ???
    - How should we think about conda-build and mamba-build (boa)?
    - (ED) What learnings can we as a community gather about the ways people have used Jinja and selectors in recipes?
        - (JK) Common Jinja uses: reduce repetition; cross-platform test scripts
    - Activation scripts (unsafe!) mostly export env vars. Make it more powerful (simple templating to depend on other variables).
      - (JK) Maybe `run_env` in meta.yaml? Similar to the existing `script_env`.
          - https://github.com/conda/conda-build/issues/4833
- [x] (ED) going to work on a few CEPs, anyone else (besides Jaime cause he already agreed) interested in co-authoring? 
    - two first: 
        - cep_A: env.yaml spec
        - cep_B: lock file spec
    - then:
        - cep_C: lock-file based env management
    - reviewers:
        - Filipe, Cheng, Jannis, Srivas
    - notes:
        - JK: sophia wrote a doc
            - Found the doc links. Though am unable to open them. Appear to be owned by Anaconda (also fwded to Eric)
            - https://docs.google.com/document/d/1-XNmPJJ0XqNW5CZm7nHwCzOSOs3PdiuOCUmJ8Yuimz0
            - https://docs.google.com/document/d/1eV4fRezxHu2lg-foVRv2gq56KEbrnaA8J_14uX31ja0
            - https://docs.google.com/document/d/17gum3j1DKcy2ygapP982879NAa7sM9ihLQ-sPOdzRVc
        - `conda list`, `conda env list`
- [x] (DPC) Should we officially allocate the first 5 minutes of every meeting to socialization?
    - **12:00-12:05?** or ~~12:05-12:10?~~
    - ED: for cf meetings i always just assume first 5 mins is waiting for folks to join
    - No clear decision
    - Could make it chair's choice?
        - Do we know in adavance who the chair will be?
- [ ] 
