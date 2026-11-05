---
tags: [meeting-notes]
---
# 2026-02-04 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

1. MvN: Marius van Niekerk (@mariusvniekerk), CF (InMarket)
1. CHL: Cheng H. Lee (@chenghlee), Anaconda/conda SC/CF core
1. KZ: Klaus Zimmermann (@zklaus), Quansight
1. Wolf Vollprecht (@wolfv), prefix.dev / conda-forge
1. JK, John Kirkham (@jakirkham), NVIDIA & conda-forge/core
1. HV, Axel Obermeier (@h-vetinari), conda-forge
1. DY, Dan Yeaw (@danyeaw), Anaconda 
1. JS, Jakov Smolic (@jsmolic), Quansight
1. JL, Jannis Leidel (@jezdez), Anaconda/cf
1. JRG, Jaime Rodríguez-Guerra (@jaimergp), Quansight, CF/C, C/SC

## Introductions

- [x] Welcome OpenKylin folks!

## Announcements

- [x] CFEP vote open until 2026-02-06: https://github.com/conda-forge/cfep/pull/64
    - Two days left, and only 14 votes out of 25 active core members. Additionally 13 emeritus can vote.
- [x] RFC period open for a bunch of CEPs: https://github.com/conda/ceps/issues/147
    - Deadline 2026-02-15. Vote to start on 2026-02-16.

## From previous meetings

- [X] (HV) Use our own QEMU instead of Fedora's: discuss approach & next steps
  - https://github.com/conda-forge/docker-images/issues/320
      - IF: Also need to take care of building the image with that package.
      - MvN: Overwrite local image qemu clients with a filesystem mount?
          - IF: Can you mount just a file?
          - MvN: Recent Docker can.
      - MvN: If mounting doesn't work, you can even rebuild the image with the new qemu.
      - IF: Also consider using only userspace emulation instead of full filesystem (which require starting Docker with qemu).
- [X] (HV) Choice of RISC-V CPU architecture baseline
  - https://github.com/conda-forge/ctng-compilers-feedstock/pull/205
  - IF: Suggestion to start with rv64gc and GCC 15. Bump to rva23 and GCC 16 and new GLIBC when AlmaLinux does it too (e.g. next year).
      - MvN: By then more hardware will be available too.
      - JK: And for testing
          - IF: OpenKylin has hardware we can use for that.
  - JRG: Ubuntu 25.10 requires RV23
  - JS: Gentoo has support for rv64gc, and will probably keep that for a while.
  - JW: Ideally they want to land rva23 in conda-forge to avoid fragmentation, but the performance gap between rv64gc and rva23 is too big.
- [x] (HV) Move to macOS >=11.0; libcxx v22 will require >=11.0, leaving us little leeway.
  - https://github.com/conda-forge/conda-forge.github.io/issues/2467
  - https://github.com/conda-forge/conda-forge.github.io/pull/2721
  - https://github.com/conda-forge/conda-forge-pinning-feedstock/pull/8162
  - Potential alternative: since the split of `libcxx-devel` from `libcxx` (and `clangxx_<target> vN` depending on the matching libc++ headers, i.e. `libcxx-devel vN`), we would theoretically be able to publish libcxx v22 without raising the deployment target; as long as our default compiler version on osx is <22, the run-export of the C++ compiler would still produce builds compatible with libcxx 21 at runtime.
  - JK: When are these updates scheduled?
      - HV: Coming days or weeks?
      - JK: Ok, but let's make an announcement.
      - MvN: It's inevitable anyway, right?

## New agenda items

- [X] WV: reproducible builds now more serious! https://prefix-dev.github.io/reproducible-builds/v1.html
    - WV: Similar efforts by Google: [OSS Rebuild](https://oss-rebuild.dev). They have attestations
    - JK: Related to that, thought of using SLSA attestions?
        - WV: Interested in hearing more.
- [X] WV: pixi-gui was [released](https://prefix.dev/blog/introducing-pixi-gui)!
    - Desktop app that uses Tauri. Manages environments and runs tasks.
    - Aiming to provide a simple experience for users that don't like CLIs.
    - DY: Why released as source available and not open source?
        - WV: To prevent rebranded copies, mostly.

## Deferred to next meeting

- [ ] JRG (conda-forge): Idea to request [OSS sponsorship for blacksmith.sh](https://www.blacksmith.sh/pricing) runners.
- [ ] JRG: [Bug in CEP 19](https://github.com/conda/ceps/issues/150)
- [ ] DH: Plan to discontinue `current_repodata.json` on conda-forge; it can't be used by modern solvers and is slow to generate.
- [ ] DH: CEPs regarding development policy for the Python implementation of conda. 14-day comment period has elapsed for "[use Python API conventions in conda instead of deprecation policy](https://github.com/conda/ceps/pull/143)"; alternate new CEP "[retract deprecation policy; move policy to conda developer documentation](https://github.com/conda/ceps/pull/152)"
