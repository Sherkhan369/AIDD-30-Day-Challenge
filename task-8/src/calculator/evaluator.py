class EvaluatorError(ValueError):
    pass

def evaluate(tokens: list) -> float:
    # This is a simplified shunting-yard or direct evaluation approach.
    # For robust evaluation, a proper Abstract Syntax Tree (AST) would be built by the parser
    # and then traversed. For this basic calculator, we'll use a direct evaluation loop.

    # Operators and their precedence
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    output = []
    operators = []

    for token in tokens:
        if isinstance(token, (int, float)):
            output.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            if not operators:
                raise EvaluatorError("Unbalanced parentheses") # Should be caught by parser
            operators.pop() # Pop the '('
        elif token in precedence:
            while (operators and operators[-1] != '(' and
                   precedence.get(operators[-1], 0) >= precedence[token]):
                output.append(operators.pop())
            operators.append(token)
        else:
            raise EvaluatorError(f"Unknown token: {token}") # Should be caught by parser

    while operators:
        if operators[-1] == '(':
            raise EvaluatorError("Unbalanced parentheses") # Should be caught by parser
        output.append(operators.pop())

    # Evaluate the RPN (Reverse Polish Notation) expression
    stack = []
    for token in output:
        if isinstance(token, (int, float)):
            stack.append(token)
        elif token in precedence:
            if len(stack) < 2:
                raise EvaluatorError("Invalid expression: Not enough operands")
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    raise EvaluatorError("Division by zero")
                stack.append(a / b)

    if len(stack) != 1:
        raise EvaluatorError("Invalid expression: Too many operands or operators")

    return float(stack[0])
