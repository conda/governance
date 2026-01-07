---
tags: [meeting-notes]
---
# 2026-01-07 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

1. JRG, Jaime Rodríguez-Guerra (@jaimergp), Quansight, conda-forge/core
2. DY, Dan Yeaw (@danyeaw), Anaconda
3. BZ, Bas Zalmstra (@baszalmstra), Prefix.dev, conda-forge/core
4. WV, Wolf Vollprecht, (@wolfv), Prefix.dev, conda-forge/core
5. JS, Jakov Smolic (@jsmolic), Quansight
6. PZ, Pavel Zwerschke (@pavelzw), QuantCo
7. DJC, Daniel Ching (@carterbox), NVIDIA, conda-forge/staged-recipes
8. SC, Sophia Castellarin (@soapy1), OpenTeams
9. JK, John Kirkham (@jakirkham), NVIDIA & conda-forge/core
10. 

## Announcements

- [X] JRG: New meeting schedule for 2026! Welcome!

## New agenda items

- [X] DY: New draft CEP for Wheel Support in Repodata
    - https://github.com/conda/ceps/pull/145
    - Requesting feedback :) TL;DR: Add wheel metadata in the repodata so conda clients can directly handle their installation.
- [X] JRG: Next steps with Conditional MatchSpecs CEP
    - https://github.com/conda/ceps/pull/111
- [X] JS: conda-build v1 recipe support update
    - https://github.com/conda/conda-build/pull/5880
    - Calls rattler-build from conda-build's CLI. Detects if the recipe is v1 or not, and in that case, convert the CLI args to the ones expected by RB.
    - Question: Which CB args should be supported in the RB integrations? A lot of the CB options are not equivalent.
        - IF: CB has two different ways of passing options: the CLI, but also via .condarc. Aggregate them and then pass it to RB via CLI flags. Must (re-)initialize the `conda.base.context::context` object with args, and then pull from that.
            - For eg: https://github.com/conda-forge/conda-forge-ci-setup-feedstock/blob/63fecea568e82bda81a5994baaba15dd20aa7b89/recipe/conda_forge_ci_setup/build_utils.py#L134-L150
- [X] DJC: NVIDIA Tegra Migrator Ready for Downstream Use
    - Tegra is an ARM64 platform variant used in robotics and other mobile applications
    - non-NVIDIA feedstock maintainer may now add a tegra variant for CUDA 12.9 if they choose
    - https://github.com/conda-forge/cuda-feedstock/blob/main/recipe/doc/recipe_guide.md#building-for-arm-tegra-devices
    - Thanks Axel and Isuru for help with the YAML migrator
    - DJC: Where to post an announcement?
        - [ ] JRG: Open PR in conda-forge/conda-forge.github.io and add MD file under news/ following the style there.
        - [ ] https://github.com/conda-forge/conda-forge.github.io/pull/2710
- [X] JRG: Experiments with `py-rattler` and `conda` CLI: https://github.com/jaimergp/conda/tree/ng/conda/ng, https://github.com/jaimergp/conda-ng. Uncovered a few things needed in `rattler` for better compatibility.
- [X] WV: Security improvements about sigstore verification: CEP opened to serve the signatures under a `.sigs` endpoint (e.g. https://prefix.dev/sigstore-example/linux-64/signed-package-2.1.0-hb0f4dca_0.conda.v0.sigs), CEP: https://github.com/conda/ceps/pull/142.
    - Also looking into transparency logs, monitoring witnesses, etc. to annotate what _should_ be in the official repodata. Currently under investigation, CEP upcoming.
        - JRG: Is this useful for an "official index" that can be used as the source of truth for mirrors?
            - WV: It would be one of the building blocks for that, yes.
        - IF: What type of content is exposed in each log entry?
            - WV: TBD. It could be, for example, the hash of the package. Its existence is sufficient to explain that the package is part of conda-forge.
    - BZ: This allows for example verifying that a package in an environment actually come from a trusted source like conda-forge. This will also work if a user got the package from a mirror.
- [X] WV: Working on a large rattler-build refactor, splitting it into multiple parts. Some changes: stricter parser, extensive test suite (2k+, easy to scale up to more recipes found in CF). For end users, this would just result in clearer errors when parsing. Should be able to catch weird errors that were not caught before.
    - Will watch for breakages in version updates in case the new parsing engine is too strict.
    - It will be released soon-ish. https://github.com/prefix-dev/rattler-build/pull/2057
- [X] JRG: Who's attending FOSDEM in Brussels? End of the month, free to attend.
    - Jaime, Bas, Wolf, ?
    - Will arive on Friday, conference starts on Saturday.
    - We will have at least dinner on Friday!
    - Also OpenSSF packaging 
