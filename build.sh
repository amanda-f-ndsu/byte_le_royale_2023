#!/bin/sh
set echo off
rm -f *.pyz
cp -r ./game ./wrapper/game
python3 -m zipapp  ./wrapper -o ./launcher.pyz -c
rm -rf ./wrapper/game