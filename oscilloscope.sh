#!/bin/bash

MY_PATH="`dirname \"$0\"`"
MY_PATH="`(cd \"$MY_PATH\" && pwd )`"


source $MY_PATH/venv/bin/activate
cd $MY_PATH
python main.py
