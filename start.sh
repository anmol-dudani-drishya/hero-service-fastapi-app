#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install pipenv
python3 -m pipenv install --dev --pre
python3 vscode-env-setup.py
uvicorn main:app --reload
