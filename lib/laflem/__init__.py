"""
Main module for laflem
"""
import sys

from .flem import Flem
from .exceptions import FlemException
from .log import error_console

__version__ = "0.3.0"


def main():
    """
    Main function for laflem.
    """
    flem = Flem(version=__version__)
    args = flem.parser.parse_args()

    try:
        if args.collection:
            collection = flem.get_collection(args.collection)
            if args.module:
                module = collection.get_module(args.module)

                module.run(**args.__dict__)
                sys.exit(0)

    except Exception as error:  # pylint: disable=broad-except
        if isinstance(error, FlemException):
            error_console.print(error, style="bold red")
        else:
            error_console.print_exception()

        sys.exit(1)


if __name__ == "__main__":
    main()
