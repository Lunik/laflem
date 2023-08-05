'''
Define the Git setup module.
This module is used to setup the base Git configuration.
'''
import os
from rich.prompt import Prompt, Confirm

from laflem.log import console
from laflem.collections.base.helloworld import HelloWorldModule

from laflem.tools.requirements import load_git_library

class GitSetupModule(HelloWorldModule):
  '''
  The Git setup module.
  '''
  name = "setup"
  description = "Init Git setup module."
  version = "0.1.0"
  extra_dependencies = 'git'

  def __init__(self):
    '''
    Init the module.
    '''
    self.git = load_git_library()

  @classmethod
  def build_parser(cls, parser):
    '''
    Add arguments to the parser or options.
    '''
    config_location_group = parser.add_mutually_exclusive_group()
    config_location_group.add_argument(
      '--local',
      action='store_true',
      help='Update the local configuration.',
      default=False,
      dest='git_setup_local',
    )
    config_location_group.add_argument(
      '--global',
      action='store_true',
      help='Update the global configuration.',
      default=True,
      dest='git_setup_global',
    )
    config_location_group.add_argument(
      '--system',
      action='store_true',
      help='Update the system configuration.',
      default=False,
      dest='git_setup_system',
    )

  @staticmethod
  def _get_git_config_location(git_setup_global, git_setup_system, **_):
    '''
    Return the Git configuration location.
    '''

    if git_setup_system:
      return 'system', '/etc/gitconfig'

    if git_setup_global:
      return 'global', os.path.expanduser('~/.gitconfig')

    return 'local', os.path.join(os.getcwd(), '.git/config')

  @staticmethod
  def _update_git_config_value(config, section, key, value_type, default_value):
    prompt = {
      'str': Prompt.ask,
      'bool': Confirm.ask,
    }
    exists = config.has_section(section) and config.has_option(section, key)

    if exists:
      current_value = config.get_value(section, key)
      new_value = prompt[value_type](f"[bold blue]{section}.{key}[/]", default=current_value)
    else:
      new_value = prompt[value_type](f"[bold blue]{section}.{key}[/]", default=default_value)

    if value_type == 'bool':
      new_value = str(new_value).lower()

    config.set_value(section, key, new_value.strip())


  def _main(self, *_args, **kwargs):
    '''
    Core the module.
    '''
    config_type, config_path = self._get_git_config_location(**kwargs)
    console.print(f"Updating [bold green]{config_type}[/] Git configuration located in [bold blue]{config_path}[/]")
    config = self.git.GitConfigParser(config_path, read_only=False)

    params = [
      ('user', 'name', 'str', None),
      ('user', 'email', 'str', None),
      ('core', 'editor', 'str', 'vim'),
      ('core', 'pager', 'str', 'less'),
      ('core', 'autocrlf', 'str', 'input'),
      ('init', 'defaultBranch', 'str', 'master'),
      ('fetch', 'prune', 'bool', True),
      ('pull', 'rebase', 'bool', True),
      ('merge', 'ff', 'bool', True),
      ('push', 'autoSetupRemote', 'bool', True),
      ('push', 'rebase', 'str', 'preserve'),
    ]

    if Confirm.ask("Do you want to update the [bold green]GPG signature[/] config ?", default=False):
      params += [
        ('user', 'signingkey', 'str', None),
        ('commit', 'gpgsign', 'bool', True),
        ('tag', 'gpgsign', 'bool', True),
        ('push', 'gpgsign', 'bool', False),
        ('log', 'showSignature', 'bool', False),
        ('gpg', 'program', 'str', 'gpg2'),
      ]

    if Confirm.ask("Do you want to setup aliases ?", default=True):
      signoff = Confirm.ask("Do all commits include a [bold green]SignOff[/] ?", default=True)
      signoff_str = '--signoff' if signoff else ''

      params += [
        ('alias', 'co', 'str', f"commit {signoff_str}"),
        ('alias', 'lo', 'str', 'log'),
        ('alias', 'st', 'str', 'status'),
        ('alias', 'ph', 'str', 'push'),
        ('alias', 'pl', 'str', 'pull'),
        ('alias', 'a', 'str', 'add'),
        ('alias', 'df', 'str', 'diff'),
        ('alias', 'ck', 'str', 'checkout'),
        ('alias', 'mr', 'str', f"merge {signoff_str}"),
        ('alias', 'cp', 'str', f"cherry-pick {signoff_str}"),
        ('alias', 'br', 'str', 'branch'),
        ('alias', 'sh', 'str', 'stash'),
        ('alias', 'plh', 'str', '!git pull --rebase && git push'),
        ('alias', 'dp', 'str', '!git add . && git commit --signoff -m \'Dev\' && git push'),
      ]

    for section, key, valut_type, default_value in params:
      self._update_git_config_value(config, section, key, valut_type, default_value)
