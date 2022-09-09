#!/bin/sh
python3 -m venv $(cd "$(dirname "$1")"; pwd -P)/$(basename "$1")lib/python
ln -s $(cd "$(dirname "$1")"; pwd -P)/$(basename "$1")bin/pkgenv /usr/local/bin/pkgenv
