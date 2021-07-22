# Conda-Tools Kick-off Agenda

1. Brief Intros
    who's here?
     - Amy Williams
     - Angela Gloyna
     - Anthony Scopatz
     - Cheng Lee
     - Connor Martin
     - Crystal Soja
     - Eric Dill
     - Filipe Fernandes
     - John Kirkham
     - Jonathan Helmus
     - Johan Mabille
     - Kai Tietz
     - Keith Kraus
     - Marcel Bargull
     - Marcelo Trevisani
     - Marius van Niekerk
     - Matthew Becker
     - Megan Yancy
     - Michael Sarahan
     - Patrick Sodré
     - Peter Wang
     - Ray Donnelly
     - Raymond Douglass
     - Sebastien Awwad
     - Sylvain Corlay
     - Tadeu Manoel
     - Travis Oliphant
     - Uwe Korn
     - Wolf Vollprecht
     - Yuvi Panda
3. Goals 
    * NumFOCUS Sponsorship
    * Conda Specs
    * A place for tools to live 
    * Support for tools
    * Open Roadmap
    * 
4. Contributions
5. Agenda
    * Introductions
    * Goals - Set up new organization to
        *  Discuss conda and ecosystem specifications
        *  Put toolings in a common location
        *  Provide governance
    * Name?
        * conda-tools org (https://github.com/conda-tools) : currently owned by conda-forge
        * conda org (https://github.com/conda) : owned by Anaconda, Inc
            * Preferred by Peter
            * Has existed for considerable time
            * Community would need to take admin control over the org
                * Move conda, conda-build, etc out?
            * Phased "transition"
                * 1. Move tools to conda organization (separate governance models for projects initially)
                * 2. Common governance model for tools, especially conda, eventually, hopefully, maybe...
            * What is the criteria for a project to be included in the conda organization
                * Balance easy to include in org with stability
                * Developing outside of the org allows easier freedom to explore
                * Incubator organization or "tag"
                    * org seems better
                    * incubator has not worked well in Jupyter, JEPs are needed for electing projects to the core org. 
                        * Incubation process rarely used
                        * Projects tend to be developed "out in the world" and added directly to Jupyter without incubation
                * When a project is moved to "core", there is a maintainance burden.  Incubating projects are more experimental
                * Moving to a incubating org allows projects to continue when developers leave companies.  
                    * Critia for inclusion should be minimal
                    * Automated process
        * SnakePit (https://github.com/TheSnakePit): QuantStack lead (mamba, boa, quetz)
        * Other random name
            * Can the conda name be used?
                * Peter + Travis are okay with use and do not major concerns
                * Peter has concern about non-participants hijacking (strip mining) the community
                * How do we protect ourselves from these type of actions?
                    * Form a consortium 
                * mamba, boa and quetz do not use "conda" to avoid trademark infringement
                    * Might change if there were rules for using the conda name 
                * Papertrail giving conda-forge and other communities permission to use the conda "name"
            * bioconda related?
    * Specifications
        * Compatibility vs Maintainance
        * Would like to see a voting aspect to specification
        * Roadmap for specs
    * Support
        * In phase one, support would be provided by the projects themselves
        * 
7. Governance
    * Proposal: Use conda-forge governance doc for this, modify for use case
    * core group is ~folks on this call
    * Commit rights should be maintained as projects move to new organizations
    * Initially individual projects would retain their own governance but be under the conda organization
    * Bootstrapping voting body
        * allow ppl to sign up, you have to vote to be in
    * README should include who runs them (Anaconda, QuantStack, individuals).  Should include information on what level of support is provided and how to ask for it 
9. What should we call ourselves?
    * Can we use the conda org?
    * Respecting the conda trademark 
        * [scopatz] - I think uses such as in conda-forge or conda-lock  fall under fair use as long as we don't then go and and try to trademark those conda-forge itself: https://en.wikipedia.org/wiki/Fair_use_(U.S._trademark_law)


# Other notes / discussions
* Where to have ongoing conversations? 
    * New slack org? Slack channel on existing slack workspace?
    * maybe gitter?


# Next Steps
* How do we continue the conversions
    * https://github.com/conda-incubator (yay!)
    * Slack!
    * https://join.slack.com/t/conda-tools/shared_invite/zt-g0907dnm-FgXZrDkZ3WdcTNhg6d3ffQ
    * weekly or fortnightly call to keep things moving
    