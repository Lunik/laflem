"""
Define the helloworld module.
This module is used to print an "Hello World!".
This is a demonstration module.
"""

from laflem.log import console
from laflem.exceptions.modules import ModuleNotRunnable


class HelloWorldModule:
    """
    The helloworld module.
    """

    name = "helloworld"
    description = "Just an Hello World module."
    version = "0.1.0"

    def _check(self, *_args, **_kwargs):
        """
        Check if the module can be run.
        """
        return True, ""

    def _main(self, *_args, **_kwargs):
        """
        Core of the module.
        """
        console.print(
            r"""
 _  _     _ _      __      __       _    _ _ 
| || |___| | |___  \ \    / /__ _ _| |__| | |
| __ / -_) | / _ \  \ \/\/ / _ \ '_| / _` |_|
|_||_\___|_|_\___/   \_/\_/\___/_| |_\__,_(_)
""",
            style="bold green",
        )

    def run(self, *_args, **_kwargs):
        """
        Run the module.
        """
        check, message = self._check(*_args, **_kwargs)
        if not check:
            raise ModuleNotRunnable(message)

        self._main(*_args, **_kwargs)

    @classmethod
    def build_parser(cls, parser):
        """
        Add arguments to the parser or options.
        """
