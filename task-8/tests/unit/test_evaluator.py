import pytest

# Assuming an 'evaluate' function will be in src/calculator/evaluator.py
# This test will initially fail (Red Phase)

def test_basic_arithmetic_evaluation():
    from src.calculator.evaluator import evaluate
    # These tests assume the input to evaluate is already a parsed structure,
    # but for now, we'll pass simple values or representations.
    # The actual input type will be refined during parser implementation.

    # Placeholder: Assuming evaluate takes a simple structure or processed input
    # For red phase, we can simulate parsed input directly or use simple numbers
    assert evaluate(5, '+', 3) == 8
    assert evaluate(10, '-', 4) == 6
    assert evaluate(2, '*', 6) == 12
    assert evaluate(10, '/', 2) == 5.0


def test_single_number_evaluation():
    from src.calculator.evaluator import evaluate
    assert evaluate(42) == 42

def test_operator_precedence_evaluation():
    from src.calculator.evaluator import evaluate
    # These tests assume a simplified structure that the evaluator processes
    # The actual structure will come from the parser
    # Example: evaluate([1, '+', 2, '*', 3]) should result in 7
    # For the red phase, we'll use a direct evaluation for a compound expression

    # This test will require the evaluator to correctly handle precedence
    # For simplicity in the red phase, we're assuming the 'evaluate' function
    # will be capable of receiving a representation that allows for precedence testing.
    # A more robust test would involve a parsed AST.
    # For now, let's assume the evaluate function can take a string for this test.
    assert evaluate("1 + 2 * 3") == 7.0 # Expect 7 (2*3=6, 1+6=7)
    assert evaluate("(1 + 2) * 3") == 9.0 # Expect 9 ((1+2)=3, 3*3=9)
    assert evaluate("10 - 4 / 2") == 8.0 # Expect 8 (4/2=2, 10-2=8)

def test_division_by_zero_error_handling():
    from src.calculator.evaluator import evaluate
    with pytest.raises(ValueError, match="Division by zero"): # Expecting ValueError
        evaluate("5 / 0")
