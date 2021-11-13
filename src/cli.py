import argparse
from typing import Sequence


class CLI:
    def __init__(self, description: str, args: Sequence[str]):
        self._cli_args = args
        self._parser = argparse.ArgumentParser(description=description)

    def set_up_log(self) -> None:
        pass

    def logfile(self) -> str:
        # TODO: yyyy-mm-dd/hh-mm-ss-hash-name.log
        return self._args.logdir + '/ost.log'

    def epilog(self) -> str:
        return self._args.logdir

    def parse_args(self) -> None:
        self._parser.add_argument(
            '-V', '--version', action='count', help='show application version')
        self._parser.add_argument(
            '-v', '--verbose', action='count', default=0,
            help='Verbose output (repeat to increase)')
        self._parser.add_argument(
            '--logdir', default='logs', metavar='DIR',
            help='logs are stored in this directory')
        self._args = self._parser.parse_args(args=self._cli_args)
