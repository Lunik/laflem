"""
Defined collection exceptions.
"""

from .base import FlemException


class CollectionNotFound(FlemException):
    """
    Raised when a collection is not found.
    """
