"""
Test case for Task 1
AI used to determine what kind of tests I should create. Resulted in three tests, the returned string, print, and return type.
"""
import sys
sys.path.append('..')
import pytest
from task1 import hello_world

def test_hello_world_type():
    """
    Test that return is a str.
    """
    result = hello_world()
    assert isinstance(result, str)

def test_hello_world_return():
    """
    Test that hello_world returns the correct message.
    """
    result = hello_world()
    assert result == "Hello World!"

def test_hello_world_print(capsys):
    """
    Test that hello_world prints the correct message.
    """
    hello_world()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello World!"
