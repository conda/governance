x---
tags: [meeting-notes]
---
# 2025-02-12 Conda Community Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Jaime Rodríguez-Guerra | JRG      | Quansight/SC | jaimergp         |
| Cheng H. Lee           | CHL      | Anaconda/CF  | chenghlee        |
| Filipe Fernandes       | FF       | conda-forge  | ocefpaf          |
| Matthew R. Becker      | MRB      | conda-forge  | beckermr         |
| Travis Hathaway        | TH       | Anaconda     | travishathaway   |
| Jonathan Helmus        | JJH      | Anaconda     | jjhelmus         |
| Daniel Ching           | DJC      | NVIDIA/CF    | carterbox        |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |

X people in total

## Introductions

- [ ]

## Announcements

- [ ]

## New Agenda Items

- [ ] (WV) Announce GSOC ideas
    - [ ] Submitted for `conda` org (lower prio given more recent age)
    - [ ] Ideas: 
        - [ ] WebAssembly
        - [ ] Security improvements in rattler (sandbox client-side scripts like activation, post-link, maybe even figure out sandboxing on Windows)
    - [ ] (FF) Better chance to have both topics selected if one idea goes to conda-forge and the other to conda
- [ ] (WV) Discuss `cache` behavior for v1 recipe format
    - [ ] https://github.com/conda/ceps/pull/102
    - [ ] See discussion at https://github.com/conda/ceps/pull/102/files#r1861339238 and points raised by Daniel Ching
    - [ ] Daniel Ching will contribute some exemplar use cases to the CEP
- [ ] (WV) Run exports in repodata ready for vote
    - [ ] https://github.com/conda/ceps/pull/108
    - [ ] Concerns about extra size no longer apply thanks to the smaller size in shards
    - [ ] Preview already available in prefix.dev, good results; allows a few optimizations
    - [ ] Patch run_exports?
- [ ] (TH) Thoughts on PyPI interoperability?
    - [ ] See this thread for background: https://conda.zulipchat.com/#narrow/channel/457607-general/topic/PyPI.20interop
    - [ ] Currently, we want better pypi interoperability libraries in rattler
    - [ ] This is available in `uv` but its not stable or likely to be published on crates.io
    - [ ] Alternative being considered is bringing over work from rip (https://github.com/prefix-dev/rip)
    - [ ] We could later wrap these libraries and make them available via py-rattler so conda plugins can utilize them (e.g. conda-pypi)
