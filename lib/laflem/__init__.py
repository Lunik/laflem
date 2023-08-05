'''
Root module for laflem
'''

import sys
import argparse

from laflem.exceptions import CollectionNotFound
from laflem.log import error_console

from .collections.base import BaseCollection
from .collections.git import GitCollection

__version__ = '0.1.3'

class FlemParser(argparse.ArgumentParser):
  '''
  Custom python parser for laflem.
  '''
  def error(self, message):
    '''
    Print an error message and exit.
    '''
    error_console.print(f"error: {message}\n", style="bold red")
    self.print_help()
    sys.exit(2)

class Flem:
  '''
  Root class for laflem.
  '''
  collections = {
    'base': BaseCollection,
    'git': GitCollection,
  }

  def get_collection(self, name):
    '''
    Return an instance of the requested collection if it exists.
    Else raise a CollectionNotFound exception.
    '''
    if name in self.collections:
      return self.collections[name]()

    raise CollectionNotFound(name)

  @property
  def parser(self):
    '''
    Construct the parser for laflem.
    Returns an instance of FlemParser.
    '''
    parser = FlemParser(description='Process some integers.')

    subparsers = parser.add_subparsers(help='collection', dest='collection')
    subparsers.required = True
    for collection in self.collections.values():
      collection_parser = subparsers.add_parser(collection.name, help=collection.description)
      collection.build_parser(collection_parser)

      collection_subparsers = collection_parser.add_subparsers(help='module', dest='module')
      collection_subparsers.required = True
      for module in collection.modules.values():
        module_parser = collection_subparsers.add_parser(module.name, help=module.description)
        module.build_parser(module_parser)

    return parser
