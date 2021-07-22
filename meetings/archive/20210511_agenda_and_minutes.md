# 2021-05-11 Conda Community Meeting

* [Meeting link](https://meet.google.com/owq-kbca-abk)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/Chicago/2021-05-11/12:00/b/Conda%20community%20meeting)
* [Last Meeting's Agenda and Minutes](https://github.com/conda-incubator/governance/tree/master/meetings)


## Attendees

| Name               | Initials | Affiliation   | GH Username     |
| ------------------ | -------- |-------------- | --------------- |
| Cheng H. Lee       | CHL      | Anaconda      | @chenghlee      |
| Marcel Bargull     | MB       | Bioconda/cf   | @mbargull       |
| CJ Wright          | CJ       | Citadel/cf    | @CJ-Wright      |
| Sebastien Awwad    | SA       | Anaconda      | @awwad          |


### Introductions
* Dan Meador (Anaconda)


### Announcements

* Anaconda Individual Edition 2021.04 releasing this week.  In addition to updates, adds linux-aarch64 (Neoverse N1/N2) and linux-s390x as supported platforms.
* Anaconda (distro & platform) is hiring.
* Citadel (HPC env and pkg management, contact CJ), is hiring.


### Standing Items

* Conda Community website mockups
* Outreach to invite more organizations to join this meeting


### New Agenda Items

* Expect conda 4.10.2 release in the next week or two.
    * Roadmap: https://github.com/conda/conda/milestone/50
    * `conda env create` (snakemake, conda lock) vs `conda create`
        * `env` spec files seem preferred (channels, pip, etc.)
        * micromamba create reads yaml files
            * includes (undocumented) extension that allows platform-specific selection
            * (CHL) willing to pull that into conda itself; document in environment schema.
* CentOS (8) EOL
    * Anaconda "defaults": supporting CentOS 7 (glibc 2.17) as default target until it hits EOL in 2024.  If newer glibc needed to build something, will use older, supported versions of Ubuntu or Debian.
    * conda-forge discussion: https://github.com/conda-forge/conda-forge.github.io/issues/1432
        * yum requirements, CDTs -> but we can wait till 2024
    * consider other community-maintained alternatives like Rocky Linux
    * commercial interest in staying on RHEL (or other rpm-based distros)
    * adding `__glibc` run constrains
        * explicit in recipes; run_exports in compiler, sysroot packages; feature in conda build
        * need to consider what manylinux, other HPC centers, other communities (e.g., nix; R) plan to do
        * roll our own glibc? Need to consider patches, kernels, etc.
* Thinking through how to handle compatibility with system packages (glibc, X11, etc.)
* `yanked` vs `broken`: ways to remove or hide packages from the ecosystem
* repodata timestamping (or other version management) for reproducibility --- bioconda


### Outstanding Items From the Previous Meeting


### Active Votes


### Subteam Updates


### Open PRs


## Discussion


## Action items


## Last meeting points (2020-05-11)