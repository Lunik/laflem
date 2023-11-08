"""
Define the Virtualenv activate module.
This module is used to activate a new virtualenv.
"""
import os
import sys

from laflem.log import console
from laflem.collections.base.helloworld import HelloWorldModule

from .const import VIRTUALENV_DEFAULT_FOLDER_NAME, PACKAGE_NAME


class VirtualenvActivateModule(HelloWorldModule):
    """
    The Virtualenv activate module.
    """

    name = "venv-activate"
    description = "Activate Virtualenvs."
    version = "0.1.0"

    @classmethod
    def build_parser(cls, parser):
        """
        Add arguments to the parser or options.
        """
        parser.add_argument(
            "--name",
            "-n",
            action="store",
            required=True,
            dest="python_virtualenv_activate_name",
            help="The name of the virtualenv.",
        )

    def _main(self, *_args, **kwargs):
        """
        Core the module.
        """
        # pylint: disable=line-too-long
        venv_path = f"{os.path.expanduser('~')}/.{PACKAGE_NAME}/python/{VIRTUALENV_DEFAULT_FOLDER_NAME}/{kwargs['python_virtualenv_activate_name']}"

        if not os.path.exists(venv_path):
            console.print(
                f"No [bold red]Virtualenv[/] with name [bold green]{kwargs['python_virtualenv_activate_name']}[/] found."
            )
            sys.exit(1)

        console.print(
            f"To activating [bold blue]Virtualenv[/] at [bold green]{venv_path}[/] run :"
        )
        console.print(f"\n  > source {venv_path}/bin/activate\n")
