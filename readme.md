# Command-line application template

This is a trivial Python CLI application that includes

- Command-line parsing
- Logging
- Testing

## Testing

### Linux/MacOS

	$ scripts/test.sh -v

Or manually

	$ source venv/bin/activate
	$ pytest -v

### Windows

    PS> scripts\test.bat

## One-time setup

### Linux/MacOS

	$ python3 -m venv venv
	$ scripts/install-libs.sh

### Windows

    PS> python -m venv venv
    PS> scripts\install-libs.bat
