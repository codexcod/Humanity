#!/bin/bash

python3.9 -m venv venv

source venv/bin/activate

python3 -m pip install -r requirements.txt

cd codigo/

python3.9 pruebita.py

