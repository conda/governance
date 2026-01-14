---
tags: [meeting-notes]
---
# 2026-01-14 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

1. JRG: Jaime Rodríguez-Guerra (@jaimergp), Quansight
1. JS: Jakov Smolic (@jsmolic), Quansight
1. KZ: Klaus Zimmermann (@zklaus), Quansight
1. MRB: Matthew R. Becker (@beckermr)
1. MvN: Marius van Niekerk (@mariusvniekerk)

## Announcements

<!-- New releases, upcoming changes, ongoing votes --->

- [X] JRG: Ongoing vote to graduate conda-pypi to conda: https://github.com/conda/governance/issues/331

## New agenda items

- [X] KZ: Update free-threading support list: https://github.com/conda-forge/conda-forge-pinning-feedstock/pull/8122.
    - KZ: Since the allow-list sends rebuilds for dependencies, but it may be ok to just open it up for all packages after a couple months?
        - MRB: Concerns about GIL being re-enabled because a package with no support prompted that.
        - MvN: Can we add an import test (or similar) to make sure this doesn't happen?
        - KZ: You do get a warning. Maybe we can turn into an error?
        - MvN: There's an env var that forces the GIL not to be re-enabled and error out. https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_GIL
- [X] KZ: qt-webengine cross-compiled builds for Linux ARM in the GPU x64 server doesn't work. Alternatives to get this rolling?
    - JRG: 
        - Get cirrus runners for linux ARM (needs credit card by NF)
            - MRB: Sent email to NF
        - Implement multistage builds with in-progress artifacts passing.
            - MRB: Maybe not worth the hassle for the small % of packages that need it.
        - Invoke CFEP-05 with local builds compiled on Docker on Apple Silicon
