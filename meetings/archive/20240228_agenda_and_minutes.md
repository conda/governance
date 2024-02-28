---
tags: [meeting-notes]
---
# 2024-02-28 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Marcel Bargull         | MB       | Bioconda/cf  | mbargull         |
| Filipe Fernandes       | FF       | conda-forge  | ocefpaf          |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Travis Hathaway        | TH       | Anaconda     | travishathaway   |
| Klaus Zimmermann       | KZ       | Quansight    | zklaus           |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Daniel Holth | DH | Anaconda | dholth |
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

- [x] (CHL) PyCon 2024 and other conferences; anyone attending?
    - Anaconda might have some presence at PyCon US
    - Some Anconda/conda folks helping to organizing PyCon US packaging summit
    - WV at PyCon US (talk), PyCon DE, SciPY US
- [X] (TH) New plugin settings hook planned for hopefully being released in 24.03.x
    - Allows plugin authors to define their own settings
    - These plugins will be accessible under `plugins.*` in config files
    - Settings will be accessible under `CONDA_PLUGINS_*` in environment variables
    - More information in the PR: https://github.com/conda/conda/pull/13554
-  [x] (JRG) [CEP-15](https://github.com/conda-incubator/ceps/blob/main/cep-15.md) and base_urls
    - Want to use this for ecosystems like Napari, Spyder
    - Implementation? I see this as the resurrection of "static metachannels" :)  :japanese_goblin:
    - [conda/conda#13137](https://github.com/conda/conda/issues/13137) still open
- [ ] (WV) New CEPs? 
  - [ ] Thinking of extras and optional dependencies.
    - https://github.com/conda-incubator/ceps/pull/55
    - Looking at PyPI, but also other ecosystems (Recommends/Suggests in deb)
    - Where to store the extras info:
      - Markers in `depends`? Could also enable win-only dependencies on noarch.
      - New field `extras={extras-name: [packages]}`
  - [ ] Tried JLAP, but thinking sharded repodata would be more performant.
    - Can be fetched in parallel, and caches more easily.
    - MB: Suggests using a small index file with the mapping, so sharding doesn't get too fine grained.
  - More recipe CEPs: cache, Jinja, tests, how the rendered recipe looks like
  - (CHL) Re-start work on microarchitecture/CPU-features dependent builds
    - https://github.com/conda-incubator/ceps/issues/59
    - https://github.com/conda-forge/staged-recipes/pull/24306
- xx 