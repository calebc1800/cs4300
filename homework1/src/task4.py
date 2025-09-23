"""
Task 4: Functions and Duck Typing
"""

def calculate_discount(price, discount):
    """
    Calculate the final price of a product after applying a given discount percentage.
    
    Args:
        price (numeric): The original price (int, float, etc.)
        discount (numeric): The discount percentage (int, float, etc.)

    Returns:
        float: The final price after discount

    Raises:
        TypeError: If price or discount are not numeric types
        ValueError: IF price is negative or discount is not between 0 and 100
    """
    # validate input types by converting to float
    try:
        price_f = float(price)
        discount_f = float(discount)
    except (TypeError, ValueError):
        raise TypeError("Price and discount must be numeric types")

    # Input value bounds
    if price_f < 0:
        raise ValueError("Price cannot be negative")

    if not (0 <= discount_f <= 100):
        raise ValueError("Discount must be between 0 and 100 percent")

    # Now the actual function
    discount_amount = price_f * (discount_f / 100)
    final_price = price_f - discount_amount

    print(f"Original price: ${price_f:.2f}")
    print(f"Discount: {discount_f}%")
    print(f"Discount amount: ${discount_amount:.2f}")
    print(f"Final price: ${final_price:.2f}")

    return final_price

if __name__ == "__main__":
    original_price = input("Enter original price of item: ")
    discount_percentage = input("Enter discount percentage: ")
    calculate_discount(original_price, discount_percentage)
