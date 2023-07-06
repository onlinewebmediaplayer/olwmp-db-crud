#!/bin/bash

sudo apt-get install python3-distutils
sudo apt-get install python3-apt
curl "https://bootstrap.pypa.io/get-pip.py" | python3

python3 -m pip install -U pip