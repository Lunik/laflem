"""
Define the Virtualenv cleanup module.
This module is used to cleanup virtualenv in the system.
"""
import os
import shutil
from rich.prompt import Confirm

from laflem.log import console
from laflem.collections.base.helloworld import HelloWorldModule

from .const import VIRTUALENV_FOLDER_NAMES


class VirtualenvCleanupModule(HelloWorldModule):
    """
    The Virtualenv cleanup module.
    """

    name = "venv-cleanup"
    description = "Cleanup Virtualenvs."
    version = "0.1.0"

    def _main(self, *_args, **_kwargs):
        """
        Core the module.
        """
        count_removed = 0

        for root, dirs, _files in os.walk(os.path.expanduser("~")):
            for directory_name in dirs:
                if directory_name in VIRTUALENV_FOLDER_NAMES:
                    full_path = f"{root}/{directory_name}"

                    if Confirm.ask(
                        f"Delete [bold blue]Virtualenv[/] [bold green]{full_path}[/] ?"
                    ):
                        shutil.rmtree(full_path)
                        console.print(
                            f"Deleted [bold blue]Virtualenv[/] at [bold red]{full_path}[/]"
                        )
                        count_removed += 1

        console.print(
            f"Removed [bold blue]{count_removed}[/] [bold blue]Virtualenvs[/]"
        )
