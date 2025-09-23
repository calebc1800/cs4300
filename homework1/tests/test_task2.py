"""
Test cases for Task 2
"""

import pytest
from task2 import demonstrate_data_types


def test_demonstrate_datat_types_types():
    """
    Test that demonstrate_data_types returns correct types.
    """
    result = demonstrate_data_types()

    # Check types of values
    assert isinstance(result['integer'], int)
    assert isinstance(result['float'], float)
    assert isinstance(result['string'], str)
    assert isinstance(result['boolean'], bool)

def test_demonstrate_data_types_keys():
    """
    Test that demonstrate_data_types returns correct dict structure.
    """
    result = demonstrate_data_types()

    # Check dict keys
    expected_keys = {'integer', 'float', 'string', 'boolean'}
    assert set(result.keys()) == expected_keys

def test_demonstrate_data_types_values():
    """
    Test that demonstrate_data_types returns the correct values
    """
    result = demonstrate_data_types()

    # Check values
    assert result['integer'] == 18
    assert result['float'] == 18.189
    assert result['string'] == "Hello World"
    assert result['boolean'] == False
    