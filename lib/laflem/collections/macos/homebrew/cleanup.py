"""
Define the Homebrew cleanup module.
This module is used to cleanup Homebrew.
"""
import os
import subprocess
from rich.prompt import Confirm

from laflem.log import console
from laflem.collections.base.helloworld import HelloWorldModule
from laflem.exceptions.modules import ModuleNotRunnable

from .const import HOMEBREW_BIN_PATH


class HomebrewCleanupModule(HelloWorldModule):
    """
    The Homebrew cleanup module.
    """

    name = "homebrew-cleanup"
    description = "Cleanup Homebrew."
    version = "0.1.0"

    def _check_installed(self):
        """
        Check if Homebrew is installed.
        """
        return os.path.exists(HOMEBREW_BIN_PATH)

    def _main(self, *_args, **_kwargs):
        """
        Core the module.
        """
        if not self._check_installed():
            raise ModuleNotRunnable("Homebrew is not installed.")

        if Confirm.ask(
            "Do you want to remove unused [bold blue]Homebrew[/] packages ?"
        ):
            console.print("Removing unused [bold blue]Homebrew[/] packages...")
            subprocess.check_call([HOMEBREW_BIN_PATH, "autoremove"])

        if Confirm.ask("Do you want to do a full cleanup of [bold blue]Homebrew[/] ?"):
            console.print("Doing a full cleanup of [bold blue]Homebrew[/]...")
            subprocess.check_call([HOMEBREW_BIN_PATH, "cleanup", "--prune=all"])
