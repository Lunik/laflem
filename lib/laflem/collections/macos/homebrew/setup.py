"""
Define the Homebrew setup module.
This module is used to install Homebrew and setup the base configuration.
"""
import os
import subprocess
import tempfile
import requests
from rich.prompt import Confirm

from laflem.log import console
from laflem.collections.base.helloworld import HelloWorldModule
from laflem.exceptions.http import HTTPException

from .const import (
    HOMEBREW_INSTALL_SCRIPT_URL,
    HOMEBREW_BIN_PATH,
    HOMEBREW_PACKAGES,
    HOMEBREW_CASK_PACKAGES,
)


class HomebrewSetupModule(HelloWorldModule):
    """
    The Homebrew setup module.
    """

    name = "homebrew-setup"
    description = "Install and init Homebrew setup module."
    version = "0.1.0"

    def __init__(self):
        """
        Initialize the module.
        """
        self.installed = self._check_installed()

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
            "--force",
            "-f",
            action="store_true",
            dest="macos_homebrew_setup_force_install",
            help="Force the installation of Homebrew.",
        )
        parser.add_argument(
            "--reinstall-packages",
            "-rp",
            action="store_true",
            dest="macos_homebrew_setup_reinstall_packages",
            help="Reinstall Homebrew packages.",
        )

    def _main(self, *_args, **kwargs):
        """
        Core the module.
        """
        if self.installed and not kwargs.get("macos_homebrew_setup_force_install"):
            console.print("[bold blue]Homebrew[/] is already installed.")
        else:
            if Confirm.ask(
                "Do you want to install [bold blue]Homebrew[/]?", default=True
            ):
                console.print("Installing [bold blue]Homebrew[/]...")
                try:
                    response = requests.get(HOMEBREW_INSTALL_SCRIPT_URL, timeout=5)
                    response.raise_for_status()
                except Exception as error:
                    raise HTTPException(
                        f"Unable to download the Homebrew script : {error}"
                    ) from error

                with tempfile.NamedTemporaryFile() as temp_file:
                    temp_file.write(response.content)

                    console.print(
                        "Running the [bold blue]Homebrew[/] install script..."
                    )
                    subprocess.check_call(["/bin/bash", temp_file.name])

        if Confirm.ask(
            "Do you want to install [bold blue]Homebrew[/] packages?", default=True
        ):
            # List all installed packages and store them in a list
            installed_packages = (
                subprocess.check_output([HOMEBREW_BIN_PATH, "list"])
                .decode("utf-8")
                .split("\n")
            )

            for package, tap_name, is_cask in (
                HOMEBREW_PACKAGES + HOMEBREW_CASK_PACKAGES
            ):
                if package in installed_packages:
                    console.print(f"[bold green]{package}[/] is already installed.")
                    if not kwargs.get("macos_homebrew_setup_reinstall_packages"):
                        continue

                    if not Confirm.ask(
                        f"Do you want to reinstall [bold green]{package}[/] ?",
                        default=True,
                    ):
                        continue

                console.print(
                    f"Installing [bold green]{package}[/] with [bold blue]Homebrew[/]..."
                )
                if tap_name:
                    console.print(
                        f"Adding [bold green]{tap_name}[/] tap to [bold blue]Homebrew[/]..."
                    )
                    subprocess.check_call([HOMEBREW_BIN_PATH, "tap", tap_name])

                    package = f"{tap_name}/{package}"

                cmd = [
                    HOMEBREW_BIN_PATH,
                    "reinstall"
                    if kwargs.get("macos_homebrew_setup_reinstall_packages")
                    else "install",
                ]
                if is_cask:
                    cmd.append("--cask")
                cmd.append(package)

                subprocess.check_call(cmd)

        if Confirm.ask(
            "Do you want to configure [bold blue]Homebrew[/] behavior ?", default=True
        ):
            auto_update = Confirm.ask(
                "Should [bold blue]Homebrew[/] automatically update ?", default=False
            )
            auto_remove = Confirm.ask(
                "Should [bold blue]Homebrew[/] automatically remove unused packages ?",
                default=True,
            )

            console.print(
                "Add those lines to your [bold blue](~/.zshrc|~/.bashrc)[/] file :"
            )
            console.print(
                f"[bold green]export HOMEBREW_NO_AUTO_UPDATE={not auto_update}[/]"
            )
            console.print(f"[bold green]export HOMEBREW_AUTOREMOVE={auto_remove}[/]")
