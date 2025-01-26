import pytest
from main import *  # Importing all from the source module
def test_dummy():
	assert True
# Test generated using Keploy
def test_add_numbers_positive_integers():
    result = add_numbers(3, 5)
    assert result == 8, "Expected the sum of 3 and 5 to be 8"