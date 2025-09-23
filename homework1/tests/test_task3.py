"""
Test cases for Task 3
"""

import pytest
from task3 import check_number_sign, is_prime, first_n_primes, sum_1_to_n

class TestCheckNumberSign:
    """
    Test cases for check_number_sign function.
    """

    @pytest.mark.parametrize("number,expected", [
        (5, "positive"),
        (-3, "negative"),
        (0, "zero"),
        (3.14, "positive"),
        (-2.5, "negative"),
    ])
    def test_check_number_sign(self, number, expected):
        """
        Parameterized test for number sign checking.
        """
        assert check_number_sign(number) == expected

class TestIsPrime:
    """
    Test cases for is_prime function.
    """

    @pytest.mark.parametrize("number,expected", [
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (8, False),
    ])
    def test_is_prime(self, number, expected):
        """
        Parameterized test for prime checking.
        """
        assert is_prime(number) == expected

class TestFirstNPrimes:
    """
    Test cases for first_n_primes function.
    """

    def test_first_10_primes(self):
        """
        Test getting first 10 prime numbers.
        """
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        result = first_n_primes(10)
        assert result == expected

    def test_first_5_primes(self):
        """
        Test getting first 5 prime numbers.
        """
        expected = [2, 3, 5, 7, 11]
        result = first_n_primes(5)
        assert result == expected

    def test_first_1_prime(self):
        """
        Test getting first 1 prime number.
        """
        expected = [2]
        result = first_n_primes(1)
        assert result == expected

class TestSum1ToN:
    """
    Test cases for sum_1_to_n function.
    """

    @pytest.mark.parametrize("n,expected", [
        (1, 1),
        (5, 15),
        (10, 55),
        (100, 5050),
    ])
    def test_sum_1_to_n(self, n, expected):
        """
        Parameterized test for sum calculation.
        """
        assert sum_1_to_n(n) == expected

    def test_mathematical_formula(self):
        """
        Test against mathematical formula n *(n + 1) / 2.
        """
        for n in [1, 5, 10, 50, 100]:
            expected = n * (n + 1) // 2
            result = sum_1_to_n(n)
            assert result == expected

    def test_zero(self):
        """
        Test edge case with n = 0.
        """
        result = sum_1_to_n(0)
        assert result == 0
