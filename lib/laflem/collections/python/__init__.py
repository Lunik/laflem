"""
Define the Python collection.
"""
from laflem.collections.base import BaseCollection

from .virtualenv import (
    VirtualenvCleanupModule,
    VirtualenvCreateModule,
    VirtualenvListModule,
    VirtualenvDeleteModule,
)


class PythonCollection(BaseCollection):
    """
    The python collection.
    """

    name = "py"
    description = "The Python collection."
    modules = {
        "venv-create": VirtualenvCreateModule,
        "venv-list": VirtualenvListModule,
        "venv-delete": VirtualenvDeleteModule,
        "venv-cleanup": VirtualenvCleanupModule,
    }
