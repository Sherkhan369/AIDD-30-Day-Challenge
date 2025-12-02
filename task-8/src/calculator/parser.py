import re

class ParserError(ValueError):
    pass

def parse(expression: str) -> list:
    if not expression:
        raise ParserError("Invalid expression: Expression cannot be empty")

    # Check for invalid characters
    if not re.fullmatch(r"[0-9+\-*/().\s]+", expression):
        raise ParserError("Invalid character in expression")

    # Basic check for unbalanced parentheses
    open_paren_count = expression.count('(')
    close_paren_count = expression.count(')')
    if open_paren_count != close_paren_count:
        raise ParserError("Unbalanced parentheses in expression")

    # This is a very basic tokenization. A full parser would build an AST.
    # For now, we'll tokenize numbers, operators, and parentheses.
    tokens = []
    current_number = ""
    for char in expression:
        if char.isdigit() or char == '.':
            current_number += char
        else:
            if current_number:
                tokens.append(float(current_number) if '.' in current_number else int(current_number))
                current_number = ""
            if char.isspace():
                continue
            tokens.append(char)
    if current_number:
        tokens.append(float(current_number) if '.' in current_number else int(current_number))

    # Post-tokenization validation for invalid sequences (e.g., "1 + * 2")
    # This is a simplified check. A full parser would handle this during AST construction.
    for i in range(len(tokens) - 1):
        if isinstance(tokens[i], (int, float)) and isinstance(tokens[i+1], (int, float)):
            raise ParserError("Invalid expression: Missing operator between numbers")
        if tokens[i] in ['+', '-', '*', '/'] and tokens[i+1] in ['+', '-', '*', '/']:
            raise ParserError("Invalid expression: Consecutive operators")

    return tokens
