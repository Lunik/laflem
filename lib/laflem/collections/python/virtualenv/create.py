"""
Define the Virtualenv create module.
This module is used to create a new virtualenv.
"""
import os
import sys
import subprocess
import shutil

from laflem.log import console
from laflem.collections.base.helloworld import HelloWorldModule

from .const import VIRTUALENV_DEFAULT_FOLDER_NAME, PACKAGE_NAME


class VirtualenvCreateModule(HelloWorldModule):
    """
    The Virtualenv create module.
    """

    name = "venv-create"
    description = "Create Virtualenvs."
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
            dest="python_virtualenv_create_name",
            help="The name of the virtualenv.",
        )
        parser.add_argument(
            "--force",
            "-f",
            action="store_true",
            dest="python_virtualenv_create_force",
            help="Force the creation of the virtualenv.",
        )
        parser.add_argument(
            "--remove",
            "-r",
            action="store_true",
            dest="python_virtualenv_create_remove",
            help="Remove the virtualenv.",
        )

    def _main(self, *_args, **kwargs):
        """
        Core the module.
        """
        # pylint: disable=line-too-long
        venv_path = f"{os.path.expanduser('~')}/.{PACKAGE_NAME}/python/{VIRTUALENV_DEFAULT_FOLDER_NAME}/{kwargs['python_virtualenv_create_name']}"

        if (
            os.path.exists(venv_path) and kwargs["python_virtualenv_create_force"]
        ) or kwargs["python_virtualenv_create_remove"]:
            console.print(
                f"Removing [bold red]Virtualenv[/] at [bold green]{venv_path}[/]"
            )
            shutil.rmtree(venv_path)

        if kwargs["python_virtualenv_create_remove"]:
            return

        if not os.path.exists(venv_path) or kwargs["python_virtualenv_create_force"]:
            console.print(
                f"Creating [bold blue]Virtualenv[/] at [bold green]{venv_path}[/]"
            )
            subprocess.check_call([sys.executable, "-m", "venv", venv_path])
        else:
            console.print(
                f"[bold red]Virtualenv[/] already exists at [bold green]{venv_path}[/]"
            )

        console.print(
            f"To activating [bold blue]Virtualenv[/] at [bold green]{venv_path}[/] run :"
        )
        console.print(f"\n  > source {venv_path}/bin/activate\n")
