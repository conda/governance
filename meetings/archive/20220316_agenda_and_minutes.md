# 2022-03-16 Conda Community Meeting

* [Meeting link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/UTC/2022-03-14/17:00/b/Conda%20community%20meeting)


## Attendees

| Name                | Initials | Affiliation   | GH Username     |
| ------------------- | -------- | ------------- | --------------- |
| Dave Clements       | DPC      | Anaconda      | @tnabtaf        |
| Jannis Leidel       | JL       | Anaconda/cf   | @jezdez         |
| Cheng H Lee         | CHL      | Anaconda      | @chenghlee      |
| Bianca Henderson    | BH       | Anaconda      | @beeankha       |
| Matthew R Becker    | MRB      | cf            | @beckermr       |
| Marius van Niekerk  | MvN      | cf/VoltronData| @mariusvniekerk |
| Katherine Kinnaman  | KK       | Anaconda      | @kathatherine   |
| Filipe Fernandes    | FF       | cf            | @ocefpaf        |
| John Kirkham        | JK       | cf/NVIDIA.    | @jakirkham      |
| | | | |
| | | | |
| | | | |
| | | | |

15 people total.

## Introductions


## Announcements

- conda-forge default branch migration from "master" to "main" is done!
    - command to migrate branches in the API
    ```
    r = sess.post(
            "https://api.github.com"
            "/repos/%s/branches/%s/rename" % (repo.full_name, repo.default_branch),
            json={"new_name": "main"},
        )
    ```
- (JL) conda 4.12.0 out on defaults
    - https://github.com/conda/conda/releases/tag/4.12.0
    - https://docs.conda.io/projects/conda/en/latest/release-notes.html#id1
- (JL) conda-libmamba-solver 22.3.0 out (announcement probably tomorrow)
    - not shipping `mamba` CLI on defaults (yet); want to avoid confusion, noise of having multiple package managers available on defaults.
- (JL) Deep-dive into the libmamba-solver work, in a week: https://anaconda.cloud/closer-look-at-conda-s-new-libmamba-solver
    * (JRG) Based on deep dive docs at https://github.com/conda/conda/pull/11059 - reviews welcome (super long, sorry!)


## Standing Items


## New Agenda Items

* (DPC) [Proposing minor, non-policy change clarifications](https://github.com/conda-incubator/governance/issues/41) to the [current governance doc](https://github.com/conda-incubator/governance/blob/master/README.md). Please join the discusison if you are interested

* (JRG) constructor stack [upstreaming has started](https://github.com/conda/constructor/issues/497):
    * Still working on a pydantic-less menuinst
        * Validation will happen during build in conda-build/boa
    * Constructor and conda-standalone: role of `conda.exe/_conda.exe`
        * Request to rename to `_conda.exe` across all platforms and keep it around
            * Start as a PR/issue; will "upgrade" to CEP only if deemed necessary from discussion 
        * This would remove the need of ALWAYS having to inject python as a dependency

* (CHL/JL) Voting for [CEP 3](https://github.com/conda/ceps/pull/2) adoption
    * Will "document while doing" as we set up the vote procedure
    * ~~One week for last review of CEP; then call vote~~
    * Call vote now; 2-week voting period

* (CHL) cbc.yaml behavior; what should conda-build pick up for this scenario?
    * current behavior: - 2.0.4 since cbc keys only apply to host packages without pins
    * open question as to what the expected behavior _should_ be
    * easiest route may be to generate a warning in such situations
    * update documentation for `bar` being pinned to 1.5
 ```
    ## recipe/meta.yaml
    requirements:
      host:
        - foo >=1.1
        - bar

    ## conda_build_config.yaml
    foo:
      - 1.0
      - 1.2
    bar:
      - 1.5

    ## versions available in the configured channels...
    foo=1.0.0
    foo=1.1.0
    foo=1.2.0
    foo=1.2.1
    foo=1.9.3
    foo=2.0.4
 ```

* (JL) conda-package-handling 1.8.0 (out on cf, in queue on defaults)
    * https://github.com/conda/conda-package-handling/releases/tag/1.8.0

* (JL) constructor 3.3.0/3.3.1 (in queue on cf and defaults)
    * https://github.com/conda/constructor/releases/tag/3.3.0

* Vendoring changings in conda (in TBD release)
    * https://github.com/conda/conda/pull/11290

## Deferred Agenda Items


## Outstanding Items From the Previous Meeting

([Previous meeting notes](https://hackmd.io/GD0NBIu9SEuOCgF4-N5NHw?view).)

## Active Votes


## Subteam Updates


## Open PRs


## Discussion


## Action items


## Last meeting points


## What is this meeting for?

Various parts of the conda community gather on a regular basis.  This meeting brings together all of these sub-communities for a community wide call.
