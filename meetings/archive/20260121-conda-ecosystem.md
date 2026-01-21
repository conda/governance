---
tags: [meeting-notes]
---
# 2026-01-21 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

<!-- Use this syntax:
* Initials: Full Name (@github-username), Affiliation.
* SD: Sam Doe (@samdoe), Company
-->

1. JRG: Jaime Rodríguez-Guerra (@jaimergp), Quansight, conda-forge/core
1. ME: Marco Esters (@marcoesters), Anaconda.
1. DW: Dawn Wages (@dawnwages), Anaconda
1. TH: Travis Hathaway (@travishathaway), Anaconda
1. DY: Dan Yeaw (@danyeaw), Anaconda 
1. JL: Jannis Leidel (@jezdez), Anaconda, conda-forge/core
1. DH: Daniel Holth (@ dholth), Anaconda
1. WV: Wolf Vollprecht, (@wolfv), Prefix.dev, conda-forge/core
1. IF: Isuruf Fernando (@isuruf), OpenTeams, conda-forge/core

<!-- Delete sections that do not apply before committing to repo -->
<!-- Every agenda item must use the initials of the person adding the item -->


## Introductions

- [ ] ...

## Announcements

<!-- New releases, upcoming changes, ongoing votes --->

- [ ] JRG: conda-rattler-solver 0.0.4 is out with pretty decent compatibility with conda's UX expectations.


## New agenda items

- [X] (JRG) Review request for https://github.com/conda/governance/pull/334
- [X] (DH) CEP [to adopt Python API conventions](https://github.com/conda/ceps/blob/6868af1290ab39c1d6e634cf10a96f56e6e13f91/cep-0099.md), amend deprecation policy in conda.
    - https://github.com/conda/ceps/pull/143
    - JRG: Start RFC period for two weeks, tag steering-council. Two weeks later, start vote.
- [X] (DW) Conda communications governance - DW and Daina Bouqin
    - Open an issue with membership request on conda/governance, tag @conda/communications
    - DW will help with first round of documenting best practices to support the growing team
- [X] (WV) FOSDEM Plans.
    - CEP hackathon on Friday!
    - JRG: Create channel on Zulip.
- [X] (WV) rattler-build refactor underway with the new cache output implementation
    - https://github.com/wolfv/rattler-build-parser-tests our test suite
    - JRG: Yay! cached multi-outputs!
    - WV: Idea to use PKL to replace Jinja config language.
- [X] (WV) sigstore progress: we have an endpoint to retrieve bundles and are working on a CEP to specify that (e.g. `*.conda.sigs`)
    - New Rust implementation passes the sigstore compliance test suite passing!
    - https://github.com/conda/ceps/pull/142
    - IF: What happens when the logs expire in GHA?
        - WV: Sigstore logs are kept in transparency logs permanently, but the actual build logs will indeed expire. Would need to think about ways of storing those somewhere else.
    - https://sigstore.github.io/sigstore-conformance/
- [X] (TH) Idea for a new blog post series: You can do that with conda? Highlights some of the lesser known use cases for conda and helps promote our packaging ecosystem (first post here: https://github.com/conda/conda-dot-org/pull/309).
    - Preview at https://deploy-preview-309--conda-dot-org.netlify.app/blog/2025-12-28-you-can-install-postgresql-with-conda

## Deferred to next meeting

- [ ] (HV) Package rename [CFEP](https://github.com/conda-forge/cfep/pull/64); what are next steps? We should wrap this up
- [ ] (HV) Use our own QEMU instead of Fedora's: discuss approach & next steps
  - https://github.com/conda-forge/docker-images/issues/320 
- [ ] (HV) [tentative, pending attendance of Isuru and OpenKylin folks] Choice of RISC-V CPU architecture baseline
  - https://github.com/conda-forge/ctng-compilers-feedstock/pull/205 
- [ ] (HV) Move to macOS >=11.0; libcxx v22 will require >=11.0, leaving us little leeway.
  - https://github.com/conda-forge/conda-forge.github.io/issues/2467
  - https://github.com/conda-forge/conda-forge.github.io/pull/2721 
  - Potential alternative: since the split of `libcxx-devel` from `libcxx` (and `clangxx_<target> vN` depending on the matching libc++ headers, i.e. `libcxx-devel vN`), we would theoretically be able to publish libcxx v22 without raising the deployment target; as long as our default compiler version on osx is <22, the run-export of the C++ compiler would still produce builds compatible with libcxx 21 at runtime.
