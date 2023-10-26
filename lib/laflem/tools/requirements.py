"""
Define all tool functions to handle requirements.
"""
import subprocess
import sys
import importlib
import re
from importlib_metadata import requires
from rich.prompt import Confirm

from laflem.log import console
from laflem.exceptions.modules import ModuleMissingDependency

__package_name__ = "laflem"


def install_extra_requirements(extra):
    """
    Install extra requirements from this package.
    """
    pattern = rf""".*; extra == ['"]{re.escape(extra)}['"]"""

    requirements = []
    for requirement in requires(__package_name__):
        if re.match(pattern, requirement):
            requirements.append(requirement.split(";")[0])

    if len(requirements) <= 0:
        return True

    answer = Confirm.ask(
        f"The module require dependecies to run ({','.join(requirements)}). Install them ?"
    )
    if not answer:
        return False

    console.print("Installing requirements")
    subprocess.check_call([sys.executable, "-m", "pip", "install", *requirements])
    return True


def load_git_library():
    """
    Load the git library.
    """
    try:
        return importlib.import_module("git")
    except ImportError as error:
        if not install_extra_requirements("git"):
            raise ModuleMissingDependency(
                "Unable to run the module without the its dependency."
            ) from error
        return importlib.import_module("git")
