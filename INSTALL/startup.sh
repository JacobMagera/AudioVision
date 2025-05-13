#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd
cd INSTALL
rm setup.sh
sudo python AudioVision.py
