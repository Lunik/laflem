"""
Define the Python cache-clear module.
This module is used to clear the cache of the python package.
"""
import os
import sys
import shutil
from rich.prompt import Confirm

from laflem.log import console
from laflem.collections.base.helloworld import HelloWorldModule

from .const import PYTHON_CACHE_LOCATION


class PythonCacheClearModule(HelloWorldModule):
    """
    The Python cache-clear module.
    """

    name = "cache-clear"
    description = "Clear the cache of the python package."
    version = "0.1.0"

    @classmethod
    def build_parser(cls, parser):
        """
        Add arguments to the parser or options.
        """

    def _main(self, *_args, **_kwargs):
        """
        Core the module.
        """
        user_os = sys.platform

        if user_os not in PYTHON_CACHE_LOCATION:
            console.print(f"Your OS [bold red]{user_os}[/] is not supported.")
            sys.exit(1)

        cache_path = os.path.expanduser(PYTHON_CACHE_LOCATION[user_os])

        if Confirm.ask(
            f"Do you want to clear the cache of the python package located at [bold green]{cache_path}[/]",
            default=True,
        ):
            console.print(
                f"Clearing [bold blue]Python[/] cache at [bold green]{cache_path}[/]"
            )

            shutil.rmtree(cache_path)
