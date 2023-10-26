"""
Define the ask module.
This module is used to ask the user about him.
This is a demonstration module.
"""
from rich.prompt import Prompt

from laflem.log import console
from .helloworld import HelloWorldModule


class AskModule(HelloWorldModule):
    """
    The ask module.
    """

    name = "ask"
    description = "Ask the user about him."
    version = "0.1.0"

    def _main(self, *_args, **_kwargs):
        """
        Core the module.
        """
        name = None
        while not name:
            name = Prompt.ask("Please provide your [bold red]name[/]")
            if not name:
                console.print("Please enter your name.", style="blue")

        console.print(f"Hello, {name} !", style="green")
