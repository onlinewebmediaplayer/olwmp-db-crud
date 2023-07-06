#!/bin/bash

pip install --user -q pipreqs

for pkg in api client ; 
do
    pipreqs --force src/$pkg
    pip install -r src/$pkg/requirements.txt
done
