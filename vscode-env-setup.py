"""VSCode configuration setup.
While working with pipenv, we need to set multiple paths
in .vscode/settings.json.
This script automates the process
"""
import json
import subprocess
from pathlib import Path

import platform

locator = "which"
if platform.system() == "Windows":
    locator = "where"


def get_output_string(command):
    """Get output string from command string."""
    out_put = subprocess.check_output(command.split())
    out_put = out_put.decode("UTF-8").replace("\n", "")
    return out_put


def init():
    """Init script."""
    print("-------VSCODE ENV Setup-------")

    print("Creating .vscode/settings.json if it does not exist...")
    Path(".vscode").mkdir(parents=True, exist_ok=True)
    Path(".vscode/settings.json").touch()

    print("Preparing settings...")
    settings = dict()
    with open(".vscode/settings.json", "r") as f:
        try:
            settings = json.load(f)
        except json.JSONDecodeError:
            pass

        settings["python.pythonPath"] = get_output_string(
            "python -m pipenv run " + locator + " python"
        )
        settings["python.venvPath"] = get_output_string("python -m pipenv --venv")
        settings["python.analysis.diagnosticMode"] = "workspace"
        settings["python.languageServer"] = "Pylance"

        settings["python.formatting.provider"] = "black"
        settings["python.linting.enabled"] = True
        settings["python.linting.flake8Enabled"] = True
        settings["cornflakes.linter.executablePath"] = get_output_string(
            "python -m pipenv run " + locator + " flake8"
        )
        settings["python.formatting.blackPath"] = get_output_string(
            "python -m pipenv run " + locator + " black"
        )
        settings["python.autoComplete.addBrackets"] = True
        settings["editor.formatOnSave"] = True

    print("Writing settings to .vscode/settings.json....")
    with open(".vscode/settings.json", "w") as f:
        json.dump(settings, f, sort_keys=True, indent=4)

    print(json.dumps(settings, sort_keys=True, indent=4))


if __name__ == "__main__":
    init()
