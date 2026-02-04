---
tags: [meeting-notes]
---
# 2026-01-28 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

1. JRG: Jaime Rodríguez-Guerra (@jaimergp), Quansight, CF/C, C/SC.
1. CHL: Cheng H. Lee (@chenghlee), Anaconda, CF/C, C/SC
1. DY: Dan Yeaw (@danyeaw), Anaconda
1. JS: Jakov Smolic (@jsmolic), Quansight
1. UK: Uwe Korn (@xhochy), QuantCo, CF/C, C/SC.
1. MRB: Matthew R Becker (@beckermr), CF/C
1. SC: Sylvain Corlay (@SylvainCorlay), QuantStack
1. BZ: Bas Zalmstra (@baszalmstra), Prefix.dev, CF/C, C/SC
1. WV: Wolf Volprecht (@wolfv), Prefix.dev, CF/C, C/SC

## Announcements

- [X] JRG: Ongoing votes:
    - 2026-02-02: https://github.com/conda/governance/issues/337
    - 2026-02-06: https://github.com/conda-forge/cfep/pull/64

## From previous meetings

- [X] (HV) Package rename [CFEP](https://github.com/conda-forge/cfep/pull/64); what are next steps? We should wrap this up

## New agenda items

- [X] JRG: Starting RFC period for standards CEP. List and graph available at: https://github.com/Quansight-Labs/conda-ecosystem-sta-mgmt/issues/4
- [X] MRB: we have heroku credits for conda-forge, $40 a month for 1 year, will be moving the heroku server to either a couple of basic instances (7 a month) or one standard instance (25 a month)
- [X] SC: notebook.link
    - Uses conda ecosystem behind the scene, especially emscriptem-forge
    - Powered by rattler under the hood and webassembly
    - All done client-side
    - Includes AI Chat widgets
    - Supports snapshotting notebook states and generating links from it so it can be shared easily
        - Example: https://notebook.link/@SylvainCorlay/demo
    - Issues and reports can be posted in notebook.link's Zulip or repo.
        - https://notebook.zulipchat.com/
    - Very useful for lessons and courses! Served 1000s students concurrently at almost no cost. Replaced massive JupyterHub deployment.
- [X] DY: Demo of `conda install <wheel>` from repodata
    - Many different libraries getting together for this! conda, conda-pypi, py-rattler, conda-rattler-solver
    - Demo with local repodata draft
- [X] MRB: CDN cloning times back up at 30 - 40 minutes?
    - Used to be ~10min, but now this like 3x or 4x. Will open issue in conda/infrastructure.
- [X] JRG: conda CEP-athon in FOSDEM this Friday! Reach out on [Zulip](https://conda.zulipchat.com/#narrow/channel/559507-2026-fosdem) if interested.
- [X] SC: Coming soon: sharded repodata in libmamba.
- [X] WV: Attestations for sources in rattler-build recipes (e.g. to check PyPI attestations, GH Releases, crates, etc). CEP to follow. One more layer of supply chain security!

## Deferred to next meeting

- [ ] (HV) Use our own QEMU instead of Fedora's: discuss approach & next steps
  - https://github.com/conda-forge/docker-images/issues/320 
- [ ] (HV) [tentative, pending attendance of Isuru and OpenKylin folks] Choice of RISC-V CPU architecture baseline
  - https://github.com/conda-forge/ctng-compilers-feedstock/pull/205 
- [ ] (HV) Move to macOS >=11.0; libcxx v22 will require >=11.0, leaving us little leeway.
  - https://github.com/conda-forge/conda-forge.github.io/issues/2467
  - https://github.com/conda-forge/conda-forge.github.io/pull/2721 
  - Potential alternative: since the split of `libcxx-devel` from `libcxx` (and `clangxx_<target> vN` depending on the matching libc++ headers, i.e. `libcxx-devel vN`), we would theoretically be able to publish libcxx v22 without raising the deployment target; as long as our default compiler version on osx is <22, the run-export of the C++ compiler would still produce builds compatible with libcxx 21 at runtime.

