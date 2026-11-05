---
tags: [meeting-notes]
---
# 2026-02-18 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

1. BZ: Bas Zalmstra (@baszalmstra), CFC/CS/Prefix.dev
1. CHL: Cheng H. Lee (@chenghlee), Anaconda/CF core/conda SC
1. JRG: Jaime Rodríguez-Guerra (@jaimergp), Quansight, CF/C, C/SC
1. JS: Jakov Smolic (@jsmolic), Quansight
1. TH: Travis Hathaway (@travishathaway), Anaconda
1. DG: Dasha Gurova (@dashagurova), Anaconda
1. SC: Sophia Castellarin (@soapy1), OpenTeams
1. DJC: Daniel Ching (@carterbox), NVIDIA/CF
1. MRB: Matthew Becker, CF core
1. JK: John Kirkham (@jakirkham), NVIDIA/CF/CFC
1. DY: Dan Yeaw (@danyeaw), Anaconda
1. HV, Axel Obermeier (@h-vetinari), conda-forge
1. DH, Daniel Holth (@dholth), Anaconda

## Announcements

- [X] JRG: Multi-CEP vote open! Deadline in ~two weeks (March 2nd): https://github.com/conda/ceps/issues/147

## From previous meetings

- [X] JRG (conda-forge): Idea to request [OSS sponsorship for blacksmith.sh](https://www.blacksmith.sh/pricing) runners.
- [X] JRG: [Bug in CEP 19](https://github.com/conda/ceps/issues/150)
    - CHL: I think this technically requires a vote since it's a change to specification, but maybe it can be a quick/_pro forma_ one.
    - JRG: To check governance.
- [X] DH: Plan to discontinue `current_repodata.json` on conda-forge; it can't be used by modern solvers and is slow to generate.
    - BZ: Prefix does not use it.
    - JRG: Will you stop updating it or remove it altogether?
    - MRB: Follow a deprecation cycle, someone may be opting it explicitly. Brownouts included, if needed.
    - DH: A different option would be to asynchronously generate current_repodata.json (update conda-index to have a separate current_repodata generator, and run in a different VM). Improving repodata.json latency.
- [x] DH: CEPs regarding development policy for the Python implementation of conda. 14-day comment period has elapsed for "[use Python API conventions in conda instead of deprecation policy](https://github.com/conda/ceps/pull/143)"; alternate new CEP "[retract deprecation policy; move policy to conda developer documentation](https://github.com/conda/ceps/pull/152)"
    - HV: Sometimes a deprecation overlaps with a following one, which makes it trickier to move on from. example: https://github.com/conda/conda-build/issues/5840
    - DH: Provided context about how the deprecation policy complicates adding sharded repodata. It is hard to know what the code should be on a first pass. Long deprecation cycles make it hard to fix/improve.
    - JK: How do we want to help DH adding code like this?
    - MRB: Disambiguates deprecation cycle of removing old code where we do want deprecation cycle from new code
    - JRG: Points out the pain of developing under the current deprecation process
    - MRB: Maybe shorten deprecation period and add Python private symbols (like private `_func`)

## New agenda items

- [x] JRG: Can someone approve notes from last week please? https://github.com/conda/governance/pull/348
    - CHL: Done!
- [X] JRG: State of recipe generators: `conda skeleton` vs. `grayskull` vs. `rattler-build generate` vs. (potentially) `conda-recipe-manager` (there are ideas to build `crm bootstrap`).
    - R recipes and `conda_r_skeleton_helper`.
    - WV: pixi-build backends also generate recipes internally so maybe that's also a generator (e.g. with the upcoming R backend)
    - DH: Prototyped [conda-skeleton as a separate](https://github.com/dholth/conda-skeleton) extracted project.
    - MRB: Supports splitting skeleton from conda-build to be able to work on it separately.
    - JRG: To document existing differences and proceed with `skeleton` split.
    - CHL: Is anyone using `conda skeleton` to genereate recipes from rpms and/or luarocks? Otherwise, I'm all in favor of removing that functionality.
        - JRG/MRB/HV: Only in conda-forge, and we copied the code over, adjusting it as needed, to generate from RPMs CDTs
- [X] HV: staged recipes Zulip channel
    - No opposition to invite Travis as a reviewer trainee.
- [X] TH: Path to becoming a staged recipe reviewer.
    - Reached out to Jaime a couple months ago.
    - WV: What about having a "sponsor" to shadow and build a 1:1 relationship?
        - DJC: I agree
    - MRB: Agrees with WV, shouldn't take more than a few months.
    - HV: Also able to interact with other reviewers in the aforementioned Zulip channel.
    - JRG: To document this in conda-forge.org
    - JK: We should track this to better assess progress and readiness.
    - MRB: Maybe a reviewer leaderboard
    - HV: Grateful to Travis for wanting to be involved.
- [x] DJC: `__cuda_arch` virtual package
    - Updated nvidia-virtual-packages plugin to match latest state of CEP-XXX Virtual Packages: https://github.com/conda/ceps/pull/103
    - Looking for feedback on implementation: https://github.com/conda-incubator/nvidia-virtual-packages/pull/5
    - Side note: I heard that PEP 817 - Wheel Variants which would allow equivalent behavior for pip is approved/merged/submitted? https://github.com/python/peps/pull/4740
        - DH: It is still Draft. 817 got split into 817 + 825. See https://discuss.python.org/t/pep-817-wheel-variants-beyond-platform-tags/105860 for DPO discussion.
    - BZ: I keep a PR in rattler up-to-date to add this there as well: https://github.com/conda/rattler/pull/1863
    - DJC: Personal goal to have this deployed and GA'd by end of summer
    - MRB: Do we need a CEP for every virtual package? Wasn't the point of `conda`'s plugin system to allow experimentation & extension without a steering council vote?
        - CHL: No, we don't need a vote for every virtual package. Though if you implement virtual packages without a CEP, you have to accept the risk that some clients may not implement it, so they may be "broken" within the context of packages in a channel requiring it.
        - CHL: `__cuda_arch` is likely a special case because the [virtual package CEP being voted on](https://github.com/conda/ceps/pull/103) already requires all clients to implement `__cuda`. So (in my opinion), `__cuda_arch` should be considered an extension to an already existing mandatory virtual package.
- [x] HV: macOS updates -- [native runners](https://github.com/conda-forge/conda-forge.github.io/issues/1781) for osx-arm64, macOS 11.0
- [x] HV: status of cirrus experiment
  - CPU builds are super fast, CUDA builds seem to OOM
  - no GPU support on linux-aarch64
  - cirrus is offering OSS projects a 50% discount
  - fixed pricing of pricing cirrus is a big plus (~$75/month for a big runner that can be subdivided)
  - spending needs a vote, but we have existing funds that should be sufficient for a while
