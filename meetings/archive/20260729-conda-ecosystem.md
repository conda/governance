---
tags: [meeting-notes]
---
# 2026-07-29 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

1. DY: Dan Yeaw (@danyeaw), Anaconda
1. JRG: Jaime Rodríguez-Guerra (@jaimergp), Quansight, CF/C, CS/C
1. WV: Wolf Vollprecht (@wolfv), prefix.dev, CF/C, CS/C
1. CHL: Cheng H. Lee (@chenghlee), Anaconda, CF/C, CS/C
2. DJC: Daniel Ching (@carterbox), NVIDIA, CF/SR


## Announcements

- [X] JRG: New conda and conda-build July releases soon, with fixes that enable the `win-arm64` migration
- [X] JRG: Last chance to review repodata v3 proposal https://github.com/conda/ceps/pull/146 before the vote starts next week
- [X] WV: Started to work on iOS and Android fun CEP: https://github.com/conda/ceps/pull/183
    - Wolf showed demo of Python builds on Android and iOS from ["mobile-forge"](http://github.com/wolfv/mobile-forge) prototype channel. Devs cross-compile packages for target platform with rattler-build and a bundler tool creates the apps for iOS/Android.
- [X] WV: rattler-build steps merged
    - PR: https://github.com/prefix-dev/rattler-build/pull/2646
    - Inspired by Chainguard Melange syntax, also similar to "actions" in Github Actions.
    - This could be base for some "common build steps" in conda-forge to take care of cargo licenses and builds, etc. Also useful for Pixi build workflows.

## New agenda items

- [X] DY: conda-pypi channel blocklist / removal, patching design
    - Goal: community channel to reduce maintenance burden of manually repackaging pure python packages
    - JRG: Would like to see a declarative list of project/wheels/requirements that are exposed in the channel, with optional metadata patches
    - DY: Current channel based on Anaconda's repocore, not open source. 600K package names creates performance issues with other codebases (the whole repodata.json is around 5GB)
