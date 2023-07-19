---
tags: [meeting-notes]
---
# 2023-07-19 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation | GH Username      |
| ---------------------- | -------- | ----------- | ---------------- |
| Bianca Henderson       | BH       | Anaconda    | beeankha         |
| Cheng H. Lee           | CHL      | Anaconda/cf | chenghlee        |
| Leopold Talirz         | LT       | Microsoft   | ltalirz          |
| Jaime Rodríguez-Guerra | JRG      | Quansight   | jaimergp         |
| Daniel Holth           | DH       | Anaconda    | dholth           |
| Marcel Bargull         | MB       | Bioconda/cf | mbargull         |
| Travis Hathaway        | TH       | Anaconda    | travishathaway   |
| Wolf Vollprecht        | WV       | prefix.dev  | wolfv            |
| Katherine Kinnaman     | KK       | Anaconda    | kathatherine     |
| Dave Clements          | DPC      | Anaconda    | tnabtaf          |
| Katherine Abrikian     | KCA      | Anaconda    | kalawac          |
| Carl Anderson          | CPA      | Anaconda    | barabo           |
| Nicholas Tucker        | NT       | Anaconda    | ntucker-anaconda |
| John Kirkham           | JK       | NVIDIA/cf   | jakirkham       |
14 people in total

## Introductions

- [x] Leo, at SciPy, comp material science.  Running atomic simulations on Azure.  Microarchitectures

## Announcements

- [x] (JRG) Open CEP Votes:
  - [ ] `menuinst` v2: https://github.com/conda-incubator/ceps/pull/8
  - [ ] `run_exports.json`: https://github.com/conda-incubator/ceps/pull/51
- [x] (BH) July releases for [conda](https://github.com/conda/conda/issues/12849) and [conda-build](https://github.com/conda/conda-build/issues/4926) are underway!
  - (JRG) conda-libmamba-solver also joining the release party.

## New Agenda Items

- [x] (JK) Anaconda.org metadata updates
    - [ ] `license_url` not showing up for packages ( https://github.com/conda/infrastructure/discussions/739 )
    - [ ] Revisit `recipe_url` idea ( https://github.com/conda/conda-build/pull/2489 )
      - [ ] (JRG) Another way available with conda-build 3.26: https://github.com/conda-forge/conda-smithy/pull/1577
    - [ ] More options to sort and filter packages (e.g., subdir, build string, etc.)
    - [ ] The `anaconda copy` command with the `--replace` flag replaces both the metadata and the destination package.
        - The docs indicate it should only replace the metadata in one spot (https://github.com/Anaconda-Platform/anaconda-client/blob/master/binstar_client/commands/copy.py#L67C5-L67C111) but the error message here (https://github.com/Anaconda-Platform/anaconda-client/blob/master/binstar_client/commands/copy.py#L42) indicates it should overwrite the package too.
        - We'd like an option to only replace the metadata on the package landing page.
    - Q: Where should we raise issues like this? (Used to be a catch-all GH repo, but that seems to have been removed.)
    - KK will discuss the above with Crystal S at Anaconda.

- [x] (CHL) Should we create a citation for `conda` itself, a la [conda-forge's Zenodo entry](https://conda-forge.org/docs/user/introduction.html#how-can-i-give-credit-to-conda-forge)?
    - (DPC) Should we write a conda academic paper? That would be a lot more work.
        - There are [also SciCrunch IDs](https://scicrunch.org/resources/data/source/nlx_144509-1/search?q=conda&l=conda).
    - (JRG) Are we talking about conda the tool, the packaging approach, or the ecosystem/community?
    - (DPC) Will create Zenodo citiation for conda tool itself.  Encourage all ecosystem components to do this.
    - (LT) Zenodo would allow us to create a DOI for each conda version (via GH integration). Major plus.
        - There is a [Zenodo Github integration](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content) to pick up on versioning.

- [x] (CHL) Should we promote the [CEPs](https://github.com/conda-incubator/ceps) and [governance](https://github.com/conda-incubator/governance) repos?
    - (JRG) We've been holding off because we did not have enough GH license seats
    - (MB) Let's hold off until the NumFOCUS transition is complete.
    - Consensus: agree in spirit, but wait until the NumFOCUS transition.

- [x] (CHL,LT) Resurrecting [archspec-enabled builds](https://github.com/conda-incubator/ceps/issues/59) discussion
    - Came up at SciPy 2023 sprints.  Probably too big to discuss here; please comment ("go nuts") in issue thread :smile: 
    - (JRG) figure out how to avoid build string explosion
      (MB) plugins? think about mamba as well!
    - (MB,CHL) we should keep `features` (mostly) dead. Probably not the route we want to take to implement this.
    - (JK) Archspec could be useful for CUDA. Though maybe it would be `gpuspec` or `cudaspec`?  There is a case for ARM which NVIDIA also cares about.
      (CHL) Ideally, we'd generalize it beyond just x86 CPUs.
    - Let's revisit in two weeks to see how the GH thread has developed to figure out next steps.

- [x] (JRG) VSCode is trying to figure out how to do Python package management: https://devblogs.microsoft.com/python/python-package-management-proposal/, and there's an issue for ideas: https://github.com/microsoft/vscode-python/issues/21627
    - JRG will follow this and take ownership
    - (LT) Sarah Kaiser is in close contact VS Code

- [x] (TH) 🔌 Let's create a Fetch Plugin hook (collaboration welcome!):
    - [x] Here's the Epic https://github.com/conda/conda/issues/11821
    - [x] We'd like help on reviewing the technical specifications, actual implementation and coming up with ideas for plugins (we already have a few :wink:)
    - [x] Here's a link to the CEP we've already written: https://github.com/conda-incubator/ceps/pull/44

- [X] (DPC): Comings and goings?
    - Rachel Asquith (Anaconda): taking over Jesse's role
    - Carl Anderson (Anaconda): looking at ways to improve (cache and CDN) performance of anaconda.org
    - Kathereine Abrikian (Anaconda): Internship ends next week!  Looking for open positions after that.
