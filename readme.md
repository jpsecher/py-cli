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
