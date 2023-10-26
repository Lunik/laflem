"""
Define the Virtualenv delete module.
This module is used to delete a new virtualenv.
"""
import os
import sys
import shutil

from laflem.log import console
from laflem.collections.base.helloworld import HelloWorldModule

from .const import VIRTUALENV_DEFAULT_FOLDER_NAME, PACKAGE_NAME


class VirtualenvDeleteModule(HelloWorldModule):
    """
    The Virtualenv create module.
    """

    name = "venv-delete"
    description = "Delete Virtualenvs."
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
            dest="python_virtualenv_delete_name",
            help="The name of the virtualenv.",
        )

    def _main(self, *_args, **kwargs):
        """
        Core the module.
        """
        # pylint: disable=line-too-long
        venv_path = f"{os.path.expanduser('~')}/.{PACKAGE_NAME}/python/{VIRTUALENV_DEFAULT_FOLDER_NAME}/{kwargs['python_virtualenv_delete_name']}"

        if not os.path.exists(venv_path):
            console.print(
                f"No [bold red]Virtualenv[/] with name [bold green]{kwargs['python_virtualenv_delete_name']}[/] found."
            )
            sys.exit(1)

        console.print(
            f"Deleting [bold blue]Virtualenv[/] with name [bold green]{kwargs['python_virtualenv_delete_name']}[/]"
        )
        shutil.rmtree(venv_path)
