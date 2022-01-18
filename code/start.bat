call python -m venv .venv
call .venv/Scripts/activate
call python -m pip install --upgrade pip pipenv
call python -m pipenv install
call python vscode-env-setup.py
