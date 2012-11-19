# Introduction

seantis.dir.base allows to put dexterity objects into 1-4 categories, showing those categories in a browsable and searchable catalog.
To learn more about seantis.dir.base visit [https://github.com/seantis/seantis.dir.base](https://github.com/seantis/seantis.dir.base)

seantis.dir.roadworks builds on seantis.dir.base, adding information about ongoing roadworks in a chosen area.

# Build Status

[![Build Status](https://secure.travis-ci.org/seantis/seantis.dir.roadworks.png)](https://travis-ci.org/seantis/seantis.dir.roadworks)

# Dependencies

seantis.dir.roadworks relies on Plone 4.2+ with dexterity and seantis.dir.base

# Installation

1. Add dexterity to Plone by adding the following Known Good Set to your buildout.cfg:

        extends =
            ...
            http://dist.plone.org/release/4.2/versions.cfg

2. Add the module to your instance eggs

        [instance]
        ...
        eggs =
            ...
            seantis.dir.roadworks


3. Ensure that the i18n files are compiled by adding

        [instance]
        ...
        environment-vars = 
            ...
            zope_i18n_compile_mo_files true

4. Install dexterity and seantis.dir.roadworks using portal_quickinstaller

# License

seantis.dir.roadworks is released under GPL v2

# Maintainer

seantis.dir.roadworks is maintained by Seantis GmbH (www.seantis.ch)
