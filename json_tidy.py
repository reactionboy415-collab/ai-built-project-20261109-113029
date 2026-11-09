import json
import sys
import argparse
from typing import Optional, List

def tidy_json(input_str: str, indent: int = 4, sort_keys: bool = False) -> str:
    """
    Parses, validates, and re-formats a JSON string.
    """
    try:
        data = json.loads(input_str)
        return json.dumps(data, indent=indent, sort_keys=sort_keys)
    except json.JSONDecodeError as e:
        # Format a user-friendly error message
        error_msg = f"Invalid JSON: {e.msg} (at line {e.lineno}, column {e.colno})"
        raise ValueError(error_msg) from e

def main(args: Optional[List[str]] = None):
    parser = argparse.ArgumentParser(
        description="JSON Tidy: A tool to validate and format JSON."
    )
    parser.add_argument(
        "infile", 
        nargs="?", 
        type=argparse.FileType("r"), 
        default=sys.stdin,
        help="Input file (defaults to stdin)"
    )
    parser.add_argument(
        "--indent", 
        type=int, 
        default=4, 
        help="Number of spaces for indentation (default: 4)"
    )
    parser.add_argument(
        "--sort-keys", 
        action="store_true", 
        help="Sort dictionary keys alphabetically"
    )
    parser.add_argument(
        "--inplace", 
        action="store_true", 
        help="Modify the input file in-place (ignored for stdin)"
    )

    parsed_args = parser.parse_args(args)

    try:
        content = parsed_args.infile.read()
        if not content.strip():
            return
            
        formatted_json = tidy_json(
            content, 
            indent=parsed_args.indent, 
            sort_keys=parsed_args.sort_keys
        )

        if parsed_args.inplace and parsed_args.infile is not sys.stdin:
            with open(parsed_args.infile.name, "w") as f:
                f.write(formatted_json + "\n")
            print(f"Successfully tidied {parsed_args.infile.name}")
        else:
            print(formatted_json)

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()