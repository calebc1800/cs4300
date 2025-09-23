"""
Task 4: Functions and Duck Typing
"""

import pytest
from task4 import calculate_discount

class TestCalculateDiscount:
    """
    Test cases for calculate_discount function.
    """

    @pytest.mark.parametrize("price,discount,expected", [
        (100, 20, 80.0),
        (100.0, 20, 80.0),
        (100, 20.0, 80.0),
        (100.0, 20.0, 80.0),
        (99.99, 15.5, 84.49),
        (75.50, 25, 56.62),
        (150, 100, 0.0),
    ])
    def test_calculate_discount_valid_inputs(self, price, discount, expected):
        """
        Test calculate_discount with various valid numeric types.
        """
        result = calculate_discount(price, discount)
        assert abs(result - expected) < 0.01

class TestInputValidation:
    """
    Test input validation and error handling.
    """

    def test_negative_price(self):
        """
        Test that negative prices raise ValueError.
        """
        with pytest.raises(ValueError, match="Price cannot be negative"):
            calculate_discount(-100, 10)

    def test_invalid_discount_range(self):
        """
        Test that discount outside 0-100 range raises ValueError.
        """
        with pytest.raises(ValueError, match="Discount must be between 0 and 100 percent"):
            calculate_discount(100, -10)

        with pytest.raises(ValueError, match="Discount must be between 0 and 100 percent"):
            calculate_discount(100, 150)

    def test_non_numeric_price(self):
        """
        Test that non-numeric price raises TypeError.
        """
        with pytest.raises(TypeError, match="Price and discount must be numeric types"):
            calculate_discount("not_a_number", 10)

    def test_non_numeric_discount(self):
        """
        Test that non-numeric discount raises TypeError.
        """
        with pytest.raises(TypeError, match="Price and discount must be numeric types"):
            calculate_discount(100, "not_a_number")

    def test_both_non_numeric(self):
        """
        Test that both non-numeric inputs raise TypeError.
        """
        with pytest.raises(TypeError, match="Price and discount must be numeric types"):
            calculate_discount("price", "discount")
