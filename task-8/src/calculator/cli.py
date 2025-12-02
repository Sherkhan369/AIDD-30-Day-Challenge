import sys
from .parser import parse, ParserError
from .evaluator import evaluate, EvaluatorError

def run_cli(expression: str):
    try:
        tokens = parse(expression)
        result = evaluate(tokens)
        print(result)
        sys.exit(0)
    except (ParserError, EvaluatorError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
