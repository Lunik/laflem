"""
Define the Git setup module.
This module is used to setup the base Git configuration.
"""
import os
from rich.prompt import Prompt, Confirm

from laflem.log import console
from laflem.collections.base.helloworld import HelloWorldModule

from laflem.tools.requirements import load_git_library
from .const import GIT_DEFAULT_CONFIG_PARAMS, GIT_GPP_CONFIG_PARAMS, GIT_ALIASES_PARAMS


class GitSetupModule(HelloWorldModule):
    """
    The Git setup module.
    """

    name = "setup"
    description = "Init Git setup module."
    version = "0.2.0"
    extra_dependencies = "git"

    def __init__(self):
        """
        Init the module.
        """
        self.git = load_git_library()

    @classmethod
    def build_parser(cls, parser):
        """
        Add arguments to the parser or options.
        """
        config_location_group = parser.add_mutually_exclusive_group()
        config_location_group.add_argument(
            "--local",
            action="store_true",
            help="Update the local configuration.",
            default=False,
            dest="git_setup_local",
        )
        config_location_group.add_argument(
            "--global",
            action="store_true",
            help="Update the global configuration.",
            default=True,
            dest="git_setup_global",
        )
        config_location_group.add_argument(
            "--system",
            action="store_true",
            help="Update the system configuration.",
            default=False,
            dest="git_setup_system",
        )

    @staticmethod
    def _get_git_config_location(git_setup_global, git_setup_system, **_):
        """
        Return the Git configuration location.
        """

        if git_setup_system:
            return "system", "/etc/gitconfig"

        if git_setup_global:
            return "global", os.path.expanduser("~/.gitconfig")

        return "local", os.path.join(os.getcwd(), ".git/config")

    @staticmethod
    def _update_git_config_value(config, section, key, value_type, default_value):
        prompt = {
            "str": Prompt.ask,
            "bool": Confirm.ask,
        }
        exists = config.has_section(section) and config.has_option(section, key)

        if exists:
            current_value = config.get_value(section, key)
            new_value = prompt[value_type](
                f"[bold blue]{section}.{key}[/]", default=current_value
            )
        else:
            new_value = prompt[value_type](
                f"[bold blue]{section}.{key}[/]", default=default_value
            )

        if value_type == "bool":
            new_value = str(new_value).lower()

        config.set_value(section, key, new_value.strip())

    def _main(self, *_args, **kwargs):
        """
        Core the module.
        """
        config_type, config_path = self._get_git_config_location(**kwargs)
        console.print(
            f"Updating [bold green]{config_type}[/] Git configuration located in [bold blue]{config_path}[/]"
        )
        config = self.git.GitConfigParser(config_path, read_only=False)

        params = GIT_DEFAULT_CONFIG_PARAMS

        if Confirm.ask(
            "Do you want to update the [bold green]GPG signature[/] config ?",
            default=False,
        ):
            params += GIT_GPP_CONFIG_PARAMS

        if Confirm.ask("Do you want to setup aliases ?", default=True):
            params += GIT_ALIASES_PARAMS

        for section, key, valut_type, default_value in params:
            self._update_git_config_value(
                config, section, key, valut_type, default_value
            )
