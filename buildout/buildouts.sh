#!/bin/bash

if which wget &> /dev/null; then
    wget https://raw.github.com/seantis/seantis.dir.roadworks/master/buildout/buildout.cfg -O buildout.cfg
    wget https://raw.github.com/seantis/seantis.dir.roadworks/master/buildout/versions.cfg -O versions.cfg
    wget https://raw.github.com/seantis/seantis.dir.roadworks/master/buildout/develop.cfg -O develop.cfg
    wget https://raw.github.com/seantis/seantis.dir.roadworks/master/buildout/izug.cfg -O izug.cfg
fi

if which curl &> /dev/null; then
    curl https://raw.github.com/seantis/seantis.dir.roadworks/master/buildout/buildout.cfg -o buildout.cfg
    curl https://raw.github.com/seantis/seantis.dir.roadworks/master/buildout/versions.cfg -o versions.cfg
    curl https://raw.github.com/seantis/seantis.dir.roadworks/master/buildout/develop.cfg -o develop.cfg
    curl https://raw.github.com/seantis/seantis.dir.roadworks/master/buildout/izug.cfg -o izug.cfg
fi
