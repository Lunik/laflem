"""
Define the Virtualenv list module.
This module is used to list virtualenv in the system.
"""
import os

from laflem.log import console
from laflem.collections.base.helloworld import HelloWorldModule

from .const import VIRTUALENV_DEFAULT_FOLDER_NAME, PACKAGE_NAME


class VirtualenvListModule(HelloWorldModule):
    """
    The Virtualenv list module.
    """

    name = "venv-list"
    description = "List Virtualenvs."
    version = "0.1.0"

    def _main(self, *_args, **_kwargs):
        """
        Core the module.
        """

        venv_path = f"{os.path.expanduser('~')}/.{PACKAGE_NAME}/python/{VIRTUALENV_DEFAULT_FOLDER_NAME}"

        for venv in os.listdir(venv_path):
            full_path = f"{venv_path}/{venv}"
            console.print(f"- [bold blue]{venv}[/] located at [green]{full_path}[/]")
