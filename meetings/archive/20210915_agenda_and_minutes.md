# 2021-09-15 Conda Community Meeting

* [Meeting link](https://meet.google.com/owq-kbca-abk)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/UTC/2021-09-15/17:00/b/Conda%20community%20meeting)
* [Last Meeting's Agenda and Minutes](https://github.com/conda-incubator/governance/tree/master/meetings)


## Attendees

| Name               | Initials | Affiliation   | GH Username     |
| ------------------ | -------- | ------------- | --------------- |
| Jaime RG           | JRG      | Quansight     | @jaimergp       |
| Matthew R Becker.  | mrb.     | cf            | @beckermr       |
| Filipe Fernandes   | FF       | ocefpaf       | @ocefpaf        |
| Jannis Leidel      | JL       | Anaconda      | @jezdez         |
| Sebastien Awwad    | SA       | Anaconda      | @awwad          |
| Cheng Lee          | CHL      | Anaconda      | @chenghlee      |



### Introductions


### Announcements

* [menuinst 1.4.18](https://github.com/conda/menuinst/releases/tag/1.4.18) has been released.
* [mamba] Work has begun on a new downloader framework (https://github.com/wolfv/powerloader):
    * Adds zchunk support
    * Resumable downloads
        * Overlap with https://github.com/conda/conda/pull/10913?
    * OCI registry & S3 support
* [conda] Work happening to add libsolv solver to conda (CEP 3)
    * Experimental PoC to see if we can use libsolv in Conda directly
    * Main PR with feature branch: https://github.com/conda/conda/pull/10881
    * Overlap with parallel work on CEP 2 (plugin architecture)
    * CEP 3 draft: https://github.com/conda/ceps/pull/2
    * JRG: This ended up in a conversation about pip interoperability (missing in our PR so far) with points that we should cover in another meeting, having Filipe Lains (Quansight) attend.

### Standing Items

* Conda Community website mockups
* Outreach to invite more organizations to join this meeting


### New Agenda Items

* [CJW] Deprecation of old conda versions, `~=` and `=` matchspec not supported by older conda versions. Having repodata entries with these cause old conda to be unable to update envs.
    * To some extent conda-forge can do this by itself via repodata patches, but community consensus would be much better
    * SA: hmmm, reconciliation repodata with a matching specification version for the current environment, with that data being sufficient for conda update (then you're hosting small additional amounts of repodata per spec version). probably has to be paired with minimal override conda settings?
    * JRG: It would work like `conda update -c recovery conda` or similar.
    * All: deprecation cycle for conda?!
    * JL: And in general, better communication towards the community. CLI notices?
    * JRG: This was introduced in [3.20.5](https://github.com/conda/conda-build/blob/3.20.5/CHANGELOG.txt#L14).
        * -This should be reverted until versioned repodatas are actually taken into account.-
        * Alternative: update `conda index` to generate specs compatible with older releases.


### Outstanding Items From the Previous Meeting


### Active Votes


### Subteam Updates


### Open PRs


## Discussion


## Action items


## Last meeting points