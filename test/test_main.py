import os
import pytest
from main import *  # Importing all from the source module
def test_dummy():
	assert True
# Test generated using Keploy
def test_add_numbers_positive_integers():
    result = add_numbers(3, 5)
    assert result == 8, f"Expected 8, but got {result}"
# Test generated using Keploy
def test_serve_homepage_missing_file(monkeypatch, tmp_path):
    # Mock os.getcwd to return a directory without index.html
    monkeypatch.setattr(os, "getcwd", lambda: str(tmp_path))
    # Call the function and assert it raises an error
    with pytest.raises(FileNotFoundError):
        serve_homepage()