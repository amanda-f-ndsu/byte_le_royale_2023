#!/bin/sh
set echo off
rm -f *.pyz
cp -r ./game ./wrapper/game
mkdir ./wrapper/server/
cp -r  ./server/client ./wrapper/server/client
python3 -m zipapp  ./wrapper -o ./launcher.pyz -c
rm -rf ./wrapper/game
rm -rf ./wrapper/server