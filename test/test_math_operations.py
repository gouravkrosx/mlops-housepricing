import pytest
from src.utils.math_operations import *  # Importing all from the source module
def test_dummy():
	assert True
# Test generated using Keploy
def test_add_numbers_positive_integers():
    result = add_numbers(3, 5)
    assert result == 8, f"Expected 8 but got {result}"
# Test generated using Keploy
def test_subtract_numbers_positive_integers():
    result = subtract_numbers(10, 4)
    assert result == 6, f"Expected 6 but got {result}"
# Test generated using Keploy
def test_multiply_numbers_positive_integers():
    result = multiply_numbers(3, 7)
    assert result == 21, f"Expected 21 but got {result}"
# Test generated using Keploy
def test_divide_numbers_positive_integers():
    result = divide_numbers(20, 4)
    assert result == 5.0, f"Expected 5.0 but got {result}"
# Test generated using Keploy
def test_divide_numbers_zero_division():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide_numbers(10, 0)