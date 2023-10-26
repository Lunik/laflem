"""
Define the self laflem collection with self functionality.
"""
from laflem.exceptions import ModuleNotFound
from laflem.collections.base import BaseCollection

from .upgrade import UpgradeModule


class SelfCollection(BaseCollection):
    """
    The self collection.
    """

    name = "self"
    description = "Self collection with laflem functionality."
    modules = {
        "upgrade": UpgradeModule,
    }
