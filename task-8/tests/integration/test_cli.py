import subprocess
import sys
import pytest

# Assuming the entry point script will be src/main.py

def run_cli_command(expression):
    command = [sys.executable, "src/main.py", expression]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def test_cli_valid_expression():
    stdout, stderr, returncode = run_cli_command("2 + 3 * 4")
    assert returncode == 0
    assert stdout == "14.0"
    assert stderr == ""

def test_cli_division_by_zero_error():
    stdout, stderr, returncode = run_cli_command("5 / 0")
    assert returncode == 1  # Assuming an exit code of 1 for errors
    assert "Division by zero" in stderr # Specific error message
    assert stdout == ""

def test_cli_invalid_expression_error():
    stdout, stderr, returncode = run_cli_command("2 + * 3")
    assert returncode == 1
    assert "Invalid expression" in stderr # Specific error message
    assert stdout == ""
