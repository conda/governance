# 2022-04-13 Conda Community Meeting

* [Meeting link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/UTC/2022-04-13/17:00/b/Conda%20community%20meeting)


## Attendees

| Name                     | Initials | Affiliation   | GH Username      |
| -------------------      | -------- | ------------- | ---------------- |
| Dave Clements            | DPC      | Anaconda      | tnabtaf          |
| Cheng H. Lee             | CHL      | Anaconda      | chenghlee        |
| Matthew R Becker         | MRB      | cf            | beckermr         |
| Kartik Raj               | KR       | Python VSCode | karrtikr         |
| Filipe Fernandes         | FF       | | |
| Bianca Henderson         | BH       | Anaconda      | beeankha         |
| Katherine Kinnaman       | KK       | Anaconda      | kathatherine     |
| John Kirkham             | JK       | NVIDIA/cf     | jakirkham        |
| Mike McCarty             | MM       | NVIDIA        | mmccarty         |
| Sebastien Awwad          | SA       | Anaconda      | awwad            |
| Marcelo Duarte Trevisani | MDT      | conda-forge   | marcelotrevisani |
| | | | |
| | | | |
| | | | |
| | | | |

19 people present


## Introductions

* Kartik Raj (VS Code)


## Announcements



## Standing Items




## New Agenda Items

* (CHL/JK) Stopping `noarch: python`  builds on Anaconda defaults
    * Conflates architecture- and interpreter-version independece
    * Various kludges to get noarch working with arch-sensitive components
    * Expect further discussions as we iterate on the recipe, dependency spec format
* (KR) Discuss state of Python ext VSCode and conda
    * https://github.com/microsoft/vscode/issues/70248
    * Is `conda activate` always necessary? Is a shell always necessary? - Probably, yes (de-facto API). Without it, environment setup would likely not work correctly.
    * Details about activation in release notes here: https://github.com/conda/conda/releases/tag/4.4.0
* (JK) `test/commands` & `run_test.*` currently exclusive (unintended?)
    * https://github.com/conda-forge/conda-forge.github.io/issues/1490
    * https://github.com/conda/conda-build/issues/4427
* (JK) Transitive dependencies
    * https://github.com/conda/conda-build/issues/3308
* (JK) Setuptools deprecation affecting `load_setup_py_data`
    * https://github.com/conda/conda-build/issues/4428
    * Also impacts grayskull
    * We need to track down the PEP announcing this change
* (CHL) Propose some topic for PyCon Packaging Summit?
    * Specifying external library dependencies (brought up previously)
    * how to deal with install requirements


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
