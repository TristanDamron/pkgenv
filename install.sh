#!/bin/sh
pkgenvdir=$(cd "$(dirname "$1")"; pwd -P)/$(basename "$1")
python3 -m venv ${pkgenvdir}lib/python
ln -s ${pkgenvdir}bin/pkgenv /usr/local/bin/pkgenv
${pkgenvdir}lib/python/bin/python3 -m pip install -r requirements.txt