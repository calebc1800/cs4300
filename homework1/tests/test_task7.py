"""
Test cases for Task 7
"""

import pytest
import numpy as np
from task7 import calculate_mean, calculate_sum, calculate_std

def test_calculate_mean():
    """
    Test calculate_mean with case studies
    """
    assert calculate_mean([1, 2, 3, 4, 5]) == 3
    assert np.isclose(calculate_mean([1.5, 2.5, 3.5]), 2.5)


def test_calculate_sum():
    """
    Test calculate_sum with case studies
    """
    assert calculate_sum([1, 2, 3]) == 6
    assert calculate_sum([0, 0, 0]) == 0


def test_calculate_std():
    """
    Test calculate_std with case studies
    """
    assert np.isclose(calculate_std([1, 2, 3, 4, 5]), np.std([1, 2, 3, 4, 5]))
    assert calculate_std([5, 5, 5, 5]) == 0
