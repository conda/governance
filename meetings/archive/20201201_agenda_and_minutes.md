# 2020-12-01 Conda Community Meeting

* [Meeting link](https://meet.google.com/owq-kbca-abk)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/Chicago/2020-12-01/09:00/b/Conda%20community%20meeting)
* [Last Meeting's Agenda and Minutes](https://github.com/conda-incubator/governance/tree/master/meetings)

## Attendees

| Name | Initials | Affiliation | Username |
| ---- | -------- |------------ | -------- |
| Gonzalo Peña-Castellanos | GPC | Quansight | @goanpeca |
| Megan Yancy | MCY | Anaconda | @myancy-anaconda |
| Marius van Niekerk | MvN | Flatiron Health | @mariusvniekerk |
| Cheng Lee | CHL | Anaconda | @chenghlee |
| Eric Dill | ED | DTN | @ericdill |
| Crystal Soja | CAS | Anaconda | @csoja |
| Christopher J "CJ" Wright | CJ | Lab49 | @cj-wright |
| Keith Kraus | KK | NVIDIA | @kkraus14 |
| Filipe Fernandes | FF | IOOS | ocefpaf |
| Michael Grant | MG | Anaconda | mcg1969 |
| Connor Martin | CJM | Anaconda |@cjmartian |
| Marcel Bargull | MB | Bioconda / conda-forge | @mbargull |
| Wolf Vollprecht | WV | QuantStack / mamba | @wolfv |
| Matthew Becker | MRB | -- | @beckermr |
| Marcelo Duarte Trevisani | MDT | conda-forge | @marcelotrevisani |
| Michael Sarahan | MCS | RStudio | @msarahan |

## Agenda

* Welcome

### Announcements


### Standing Items
* Anaconda: Organizational-level CLA
    * No current updates.


### New Agenda Items

* Rotating Meeting Facilitator
    * Call for volunteers
    * Who wants to go next?

* Conda Triaging and Issue Tracking meeting took place.
    * Meeting: Kale, Marcel, Gonzalo, Cheng
    * Splitting responsibility by day: each person triages issues that come in that day
    * [conda-triage](https://conda.slack.com/archives/C01FMCT5W84)

* Given that pip install conda still "works" but obviously installs something wildly out of date and non functional should we yank the releases on pypi ? (@marius)
    * Existing blog posts refer to conda being pip installable
    * Possible solutions:
        * could `pipx install conda` with a standalone binary?
        * `pip install conda` forcibly fails with a link to miniconda installer?
        * Remove the packages but reserve the package name?
        * _Very_ long term: cool but probably impractical due to major technical challenges
    * Short term fix: Anaconda will replace with newer stub package on PyPI.
        * Create a `conda-stub` repository that creates folder with an empty package.
        * Will not remove package (without annoucement) to avoid breaking existing users & workflows.
        * Issue: https://github.com/conda/conda/issues/10388

* Where are the conda-standalone binaries these days?
    * Since all i know of is https://repo.anaconda.com/pkgs/misc/conda-execs
    * Short term I am unpacking the ones from https://anaconda.org/anaconda/conda-standalone (for use in ensureconda)
        * `conda install conda-standalone` -> installs into `$CONDA_PREFIX/standalone_conda`
        * https://repo.anaconda.com/pkgs/main/${subdir}/conda-standalone*.tar.bz2
    * Ray has pushed for updating these binaries for each conda release.
    * Anaconda needs to address internal CI issues around automating executable signing. (Currently use a manual process of downloading, re-signing, and re-uploading executables.)

* [x] (MRB) package copying and package metadata on anaconda.org
    * We are having an issue in conda-forge where when we [copy](https://api.anaconda.org/docs#!/package/post_copy_package_owner_login_package_name_version_basename) packages from one user to another using the copy API endpoint, the metadata per package (doc_url, dev_url etc) displayed on anaconda.org is erased. We need this metadata for certain packages, especially cudatoolkit.
    * We need two fixes:
        * support for patch requests for the anaconda.org `/package/{owner_login}/{package_name}` API endpoint so that we can restore the metadata
        * fix the copy endpoint so it does not delete this metadata
    * These will let us fix the packages we have and make sure it doesn't happen for new packages.
    * issue: https://github.com/Anaconda-Platform/anaconda-client/issues/556

* Audit (CJ)
	* Using depfinder to check:
		* Accurate 
		* Under specified
		* Over specified
		* Under and over specified
		* Errored
    * Link to the information
    	* https://github.com/conda-forge/by-the-numbers
        * https://github.com/conda-forge/by-the-numbers/blob/master/audit_accuracy.ipynb

* Raises the question of how to handle optional dependencies and/or sub-packages?
    * Like RPM provides?

* Additional test "keys" for conda-build (WV)
    * I wrote down some ideas here: https://github.com/mamba-org/boa/issues/93
    * Is conda-build interested in these tests? (CHL: yes; please open issue on conda-build GH)
    * Fits into concepts for conda-verify

### Outstanding Items From the Previous Meeting

* N/A

### Active Votes


### Subteam Updates


#### Open PRs

* N/A

## Discussion


## Action items

## Last meeting points (2020-11-17)

* Ways to address diversity inclusiveness issues
    * new sub-team - charter for maintaining and advancing conda-forge as a diverse community, try to grow. Charter is dynamic. Looking for those who are not core contributors of conda-forge.
    * Would like input on document
    * https://github.com/conda-forge/conda-forge.github.io/pull/1187
* Availability of artifact verification features to other pieces of software (than conda):
    * SA: @Wolf,  Please be aware that at first, we're offering the trust and signing data to paid folks, because... lights on.  But I don't see why support for consuming that data shouldn't be handled in any package manager frontend talking to the repository.  There's a project with the majority of the low-level code and a set of algorithms.  The process of integrating that into conda (or other managers) is a delicate thing, so I'm hoping that the guidelines are helpful enough... but this will improve after conda integration.
    * Wolf: sure. with quetz we're working hard to support mirroring of conda-channels (specifically conda-forge), and this trust & verification is pretty integral for that so ... we might have to implement this anyways, and then it would probably make sense to do it in the same fashion as upstream
    * SA: that'd be good, yeah. We can talk about the TUF work underlying it at the least