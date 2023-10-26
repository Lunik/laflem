"""
Define the git collection for Git functionality.
"""
import importlib

from laflem.collections.base import BaseCollection

from .setup import GitSetupModule


class GitCollection(BaseCollection):
    """
    The git collection.
    """

    name = "git"
    description = "Git collection for Git functionality."
    modules = {
        "setup": GitSetupModule,
    }
