# Quickstart: Basic Calculator

This guide provides a quick overview of how to run and use the Basic Calculator.

## Prerequisites

- Python 3.10+ installed on your system.

## Running the Calculator

1.  **Navigate to the project root directory**:

    ```bash
    cd /path/to/your/project
    ```

2.  **Execute the `main.py` script with an expression**:

    The calculator expects a single string argument which is the arithmetic expression to evaluate. Ensure the expression is enclosed in quotes to be treated as a single argument by your shell.

    ```bash
    python src/main.py "2 + 3 * 4"
    ```

    This command should output:

    ```
    14.0
    ```

## Examples

### Basic Addition

```bash
python src/main.py "10 + 5"
# Expected output: 15.0
```

### Operator Precedence

```bash
python src/main.py "(10 + 5) * 2"
# Expected output: 30.0
```

### Division

```bash
python src/main.py "10 / 4"
# Expected output: 2.5
```

### Error Handling (Division by Zero)

```bash
python src/main.py "5 / 0"
# Expected error output (to stderr): Error: Division by zero
```

### Error Handling (Invalid Expression)

```bash
python src/main.py "2 + * 3"
# Expected error output (to stderr): Error: Invalid expression
```
