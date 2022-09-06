#!/bin/sh
ln -s $(cd "$(dirname "$1")"; pwd -P)/$(basename "$1")bin/pkgenv /usr/local/bin/pkgenv