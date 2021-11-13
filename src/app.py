from cli import CLI
from constants import SUCCESS, APP_VERSION, APP_DESCRIPTION
from typing import Sequence
import sys


class App(CLI):
    def __init__(self, args: Sequence[str]):
        super().__init__(APP_DESCRIPTION, args)
        self.parse_args()
        self._check_args()

    def run(self):
        if self._args.verbose > 0:
            print(f'{APP_DESCRIPTION} v{APP_VERSION}')
        if self._args.version:
            print(APP_VERSION)

    def _check_args(self):
        needed = (self._args.version, )
        if not any(needed):
            self._parser.print_help()
            sys.exit(SUCCESS)
