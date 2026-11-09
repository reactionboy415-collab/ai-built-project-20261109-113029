# JSON Tidy

JSON Tidy is a polished command-line utility for validating and formatting JSON data. It aims to be a more user-friendly alternative to `python -m json.tool` by providing clearer error messages and more control over output formatting without any external dependencies.

## Features

- **Validation**: Check if a JSON file is syntactically correct.
- **Pretty Printing**: Reformat messy JSON with configurable indentation.
- **Key Sorting**: Optionally sort dictionary keys alphabetically.
- **Clear Errors**: Provides line and column numbers for syntax errors.
- **Piping Support**: Works with standard input (stdin) and output (stdout).

## Setup

No installation is required other than having Python 3.6+ installed. 

You can run the script directly:
```bash
python json_tidy.py --help
```

Or install it in editable mode for convenience:
```bash
pip install -e .
```

## Usage

### Format a file in-place
```bash
python json_tidy.py data.json --inplace
```

### Print formatted output to console
```bash
python json_tidy.py data.json
```

### Format with custom indentation and sorted keys
```bash
python json_tidy.py data.json --indent 2 --sort-keys
```

### Use with pipes
```bash
cat data.json | python json_tidy.py
```

## Project Structure

- `json_tidy.py`: The main CLI logic.
- `test_json_tidy.py`: Comprehensive test suite using the standard `unittest` library.
- `pyproject.toml`: Basic project metadata for Python packaging.

## Limitations

- Designed for standard JSON; does not support JSON5 or comments (C-style).
- Large files (hundreds of megabytes) are loaded into memory for processing.

## Contributing

Feel free to fork the repository and submit pull requests. Ensure that all tests pass by running:
```bash
python -m unittest test_json_tidy.py
```