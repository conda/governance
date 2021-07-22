# 2021-05-25 Conda Community Meeting

* [Meeting link](https://meet.google.com/owq-kbca-abk)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/Chicago/2021-05-25/12:00/b/Conda%20community%20meeting)
* [Last Meeting's Agenda and Minutes](https://github.com/conda-incubator/governance/tree/master/meetings)


## Attendees

| Name               | Initials | Affiliation   | GH Username     |
| ------------------ | -------- |-------------- | --------------- |
| Cheng H. Lee       | CHL      | Anaconda      | @chenghlee      |
| matthew becker     | MRB      | conda-forge   | @beckermr       |
| Sebastien Awwad    | SA       | Anaconda      | @awwad          |
| Marcel Bargull     | MB       | Bioconda/cf   | @mbargull       |


### Introductions


### Announcements

* [AnacondaCON 2021](https://anacondacon.io/): 9 Jun, all virtual. 
* conda 4.10.2 delayed by ~1 week


### Standing Items

* Conda Community website mockups
* Outreach to invite more organizations to join this meeting


### New Agenda Items

* Planning conda-build release
    * All patches applied as binary; causes issues on Windows & how patch detection works (or doesn't)
        * https://github.com/conda/conda-build/issues/1973
        * https://github.com/conda/conda-build/pull/2035
    * Conda UTF-16 handling:
        * https://github.com/conda/conda/pull/9946
        * https://github.com/conda-forge/conda-feedstock/blob/master/recipe/gh9946_utf_16_replacement.patch
    * `sys.exit(...)` when invoking conda-build via API, rather than CLI. (Should raise Exceptions instead; developer quality-of-life improvement)

* Update to spec (conda, conda-build)
    * Support for optional deps

* Quetz: plans for authentication support
    * 5.0+ planning: authn schemes for package servers
    * Anaconda.org currently uses token-in-URL scheme
    * mamba: HTTP basic auth, anaconda.org token scheme
    * User requests for other schemes:
        * `~/.netrc`
        * RSA SecurID: https://github.com/conda/conda/pull/10667
    * (FP) Share APIs, not necessarily code, between mamba & conda for authn

* (CJ) Version 4 symbol database released!

* Packaging con --- more info next week


### Outstanding Items From the Previous Meeting


### Active Votes


### Subteam Updates


### Open PRs


## Discussion


## Action items


## Last meeting points (2020-05-11)