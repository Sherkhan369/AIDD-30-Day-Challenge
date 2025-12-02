# Data Model: Basic Calculator

This document outlines the key entities and their attributes relevant to the Basic Calculator feature.

## Entities

### Expression

Represents the mathematical expression provided as input to the calculator.

- **Description**: A string containing numbers, arithmetic operators (+, -, *, /), and parentheses.
- **Attributes**:
    - `value`: (string) The raw input string of the expression.
- **Validation Rules**:
    - Must not be empty.
    - Must contain only valid characters (digits, operators, parentheses, whitespace).
    - Must represent a syntactically valid arithmetic expression.

### Result

Represents the computed numerical outcome of evaluating an Expression.

- **Description**: The numerical value obtained after successfully evaluating the input expression.
- **Attributes**:
    - `value`: (number) The calculated numerical result.
- **Validation Rules**:
    - Must be a valid number (integer or float).
    - Special cases like `Infinity` or `NaN` (from division by zero or invalid operations) should be handled explicitly.
