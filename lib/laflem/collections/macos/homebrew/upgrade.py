"""
Define the Homebrew upgrade module.
This module is used to upgrade Homebrew packages.
"""
import os
import subprocess

from laflem.log import console
from laflem.collections.base.helloworld import HelloWorldModule
from laflem.exceptions.modules import ModuleNotRunnable

from .const import HOMEBREW_BIN_PATH


class HomebrewUpgradeModule(HelloWorldModule):
    """
    The Homebrew upgrade module.
    """

    name = "homebrew-upgrade"
    description = "Upgrade all Homebrew packages."
    version = "0.1.0"

    def _check_installed(self):
        """
        Check if Homebrew is installed.
        """
        return os.path.exists(HOMEBREW_BIN_PATH)

    @classmethod
    def build_parser(cls, parser):
        """
        Add arguments to the parser or options.
        """
        parser.add_argument(
            "--update",
            "-u",
            action="store_true",
            dest="macos_homebrew_upgrade_update",
            help="Update Homebrew.",
        )
        parser.add_argument(
            "--dry-run",
            "-d",
            action="store_true",
            dest="macos_homebrew_upgrade_dry_run",
            help="Dry run the upgrade.",
        )

    def _main(self, *_args, **kwargs):
        """
        Core the module.
        """
        if not self._check_installed():
            raise ModuleNotRunnable("Homebrew is not installed.")

        if kwargs.get("macos_homebrew_upgrade_update"):
            console.print("Updating [bold blue]Homebrew[/]...")
            subprocess.check_call([HOMEBREW_BIN_PATH, "update"])

        console.print("Upgrading [bold blue]Homebrew[/] packages...")
        cmd = [HOMEBREW_BIN_PATH, "upgrade"]
        if kwargs.get("macos_homebrew_upgrade_dry_run"):
            cmd.append("--dry-run")
        subprocess.check_call(cmd)
