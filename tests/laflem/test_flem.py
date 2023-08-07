import pytest

from laflem.flem import FlemParser

def test_flem_parser():
  '''
  Test the flem parser.
  '''
  parser = FlemParser()
  with pytest.raises(SystemExit):
    parser.error('error')
