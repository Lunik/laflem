'''
Define the MacOS collection for Mac computers.
'''
from laflem.collections.base import BaseCollection

from .homebrew import HomebrewSetupModule, HomebrewUpgradeModule, HomebrewCleanupModule

class MacOSCollection(BaseCollection):
  '''
  The macos collection.
  '''
  name = "mac"
  description = "The MacOS collection."
  modules = {
    "homebrew-setup": HomebrewSetupModule,
    "homebrew-upgrade": HomebrewUpgradeModule,
    "homebrew-cleanup": HomebrewCleanupModule,
  }

  @classmethod
  def build_parser(cls, parser):
    '''
    Add arguments to the parser or options.
    '''
