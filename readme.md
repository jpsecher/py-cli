# Command-line application template

This is a trivial Python CLI application that includes

- Command-line parsing
- Logging
- Testing

## Testing

### Linux/MacOS

	$ source venv/bin/activate
	$ pytest -v --cov

## One-time setup

### Linux/MacOS

	$ python3 -m venv venv
	$ source venv/bin/activate
	$ pip install -U pip
	$ pip install -r requirements-dev.txt
