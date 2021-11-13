# Command-line application template

This is a trivial Python CLI application that includes

- Command-line parsing
- Logging
- Testing

## Built-in functionality

`-h/--help`: Output usage instructions.

`-V/--version`: Output version number.

`-v/--verbose`: Increase verbosity level, can be repeated like `-vvv`.  All log lines below or equal to the verbosity level will be printed on stdout with time-stamp.

`-d/--logdir`: Put time-stamped log information in a unique log file in that particular directory.  All log lines will be included, no matter the verbosity level.  The location of the log will be printed at the end.

## Logging

Logging is done by eg.

    self.log(f'serial number is {self._serial}', 2)

which will log a line at verbosity level 2.  Level 0 is the default, so this log line will always be printed out:

    self.log('Starting up...')

Each log line on stdout will be prefixed by the local time:

    23:55:12 Starting up...

Each log line in the log file (if any) will be prefixed by full ISO time stamp and verbosity level:

    2021-11-25T23:55:12 [2] serial number is 3415

## Error handling

If the code raises an exception, the application will return non-zero, and print out the stack trace and the log lines back to the most recent level 0.

## TODO:

- coverage

## Testing

### Linux/MacOS

    $ scripts/test.sh -v
    $ scripts/typecheck.sh

Or manually

    $ source venv/bin/activate
    $ pytest --cov --cov-report=term-missing
    $ mypy src/app.py --strict

### Windows

    PS> scripts\test.bat

## One-time setup

### Linux/MacOS

    $ python3 -m venv venv
    $ scripts/install-libs.sh

### Windows

    PS> python -m venv venv
    PS> scripts\install-libs.bat
