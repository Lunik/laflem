"""
Define the base collection with basic functionality.
"""
from laflem.exceptions import ModuleNotFound

from .helloworld import HelloWorldModule
from .ask import AskModule


class BaseCollection:
    """
    The base collection.
    """

    name = "base"
    description = "Base collection with basic functionality."
    modules = {
        "helloworld": HelloWorldModule,
        "ask": AskModule,
    }

    def get_module(self, name):
        """
        Return an instance of the requested module if it exists.
        Else raise a ModuleNotFound exception.
        """
        if name in self.modules:
            return self.modules[name]()

        raise ModuleNotFound(name)

    @classmethod
    def build_parser(cls, parser):
        """
        Add arguments to the parser or options.
        """
