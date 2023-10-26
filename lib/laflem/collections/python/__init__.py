"""
Define the Python collection.
"""
from laflem.collections.base import BaseCollection

from .virtualenv import VirtualenvCleanupModule, VirtualenvCreateModule


class PythonCollection(BaseCollection):
    """
    The python collection.
    """

    name = "py"
    description = "The Python collection."
    modules = {
        "venv-cleanup": VirtualenvCleanupModule,
        "venv-create": VirtualenvCreateModule,
    }
