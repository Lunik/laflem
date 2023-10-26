"""
Define module exceptions.
"""

from .base import FlemException


class ModuleNotFound(FlemException):
    """
    Raised when a module is not found.
    """


class ModuleNotRunnable(FlemException):
    """
    Raised when a module is not runnable.
    """


class ModuleMissingDependency(FlemException):
    """
    Raised when a module is missing a dependency.
    """
