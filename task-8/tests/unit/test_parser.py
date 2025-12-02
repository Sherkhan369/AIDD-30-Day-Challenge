import pytest

# Assuming a 'parse' function will be in src/calculator/parser.py
# This test will initially fail (Red Phase)

def test_valid_expression_parsing():
    from src.calculator.parser import parse
    # This is a placeholder test, actual token structure depends on implementation
    assert parse("1 + 2") is not None # Expecting some parsed structure, not None
    assert parse("10 * (2 + 3)") is not None

def test_invalid_expression_parsing():
    from src.calculator.parser import parse
    with pytest.raises(ValueError, match="Invalid expression"): # Expecting ValueError for invalid input
        parse("1 + ")
    with pytest.raises(ValueError, match="Invalid character"): # Expecting ValueError for invalid character
        parse("1 $ 2")
    with pytest.raises(ValueError, match="Unbalanced parentheses"): # Expecting ValueError for unbalanced parentheses
        parse("(""1 + 2"")")
