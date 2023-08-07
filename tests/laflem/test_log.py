
from laflem.log import error_console, console

def test_error_console():
  error_console.print("test", style="bold red")

def test_console():
  console.print("test", style="bold green")
