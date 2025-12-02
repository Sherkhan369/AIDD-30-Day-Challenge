import sys
from calculator.cli import run_cli

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m src.main \"<expression>\"", file=sys.stderr)
        sys.exit(1)
    expression = sys.argv[1]
    run_cli(expression)
