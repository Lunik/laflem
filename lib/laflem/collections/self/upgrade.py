"""
Define the self upgrade module.
This module is used to upgrade laflem.
"""

import subprocess
import sys
from rich.prompt import Confirm

from laflem.log import console
from laflem.collections.base.helloworld import HelloWorldModule

from .const import PACKAGE_NAME


class UpgradeModule(HelloWorldModule):
    """
    The upgrade module.
    """

    name = "upgrade"
    description = "Upgrade laflem"
    version = "0.1.0"

    def _main(self, *_args, **_kwargs):
        """
        Core of the module.
        """
        if Confirm.ask(f"Do you wish to upgrade {PACKAGE_NAME} ?", default=True):
            console.print(f"Upgrading [bold green]{PACKAGE_NAME}[/]...")
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "--upgrade", PACKAGE_NAME]
            )
