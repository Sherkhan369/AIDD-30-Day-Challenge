# CLI Interface Contract: Basic Calculator

This document defines the interface contract for the Basic Calculator's Command-Line Interface (CLI).

## Input

**Method**: Command-line argument

**Parameter**: `expression`
- **Type**: String
- **Description**: The mathematical expression to be evaluated. It should contain numbers, standard arithmetic operators (`+`, `-`, `*`, `/`), and parentheses.
- **Constraints**:
    - Non-empty string.
    - Maximum length: 100 characters (as per SC-001).
    - Valid characters only (digits, `.` for decimals, `+`, `-`, `*`, `/`, `(`, `)`, whitespace).
    - Must be a syntactically valid arithmetic expression.

**Example Input**: `python main.py "(2 + 3) * 4"`

## Output

**Method**: Standard Output (stdout) or Standard Error (stderr)

### Success Output
- **Type**: Number (string representation)
- **Description**: The numerical result of the evaluated expression.
- **Format**: A single line containing the number.
- **Example Output**: `20.0`

### Error Output
- **Type**: String
- **Description**: An informative error message indicating why the expression could not be evaluated.
- **Format**: A single line (or multi-line, if detailed) sent to stderr.
- **Error Taxonomy**:
    - `Invalid Expression`: For malformed syntax or unsupported characters.
    - `Division by Zero Error`: When an attempt to divide by zero is detected.
    - `Arithmetic Error`: For other calculation issues (e.g., overflow, underflow - though less likely with basic operations).
- **Example Error Output (stderr)**: `Error: Division by zero`
