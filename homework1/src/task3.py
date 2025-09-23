"""
Task 3: Control Structures
"""

def check_number_sign(n):
    """
    Check if a given number is positive, negative, or zero.

    Args:
        number (int/float): The number to check

    Returns:
        str: 'positive', 'negative', or 'zero'
    """
    if n > 0:
        result = "positive"
    elif n < 0:
        result = "negative"
    else:
        result = "zero"

    print(f"The number {n} is {result}")
    return result

def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n (int): Number to check

    Returns:
        bool: True if prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def first_n_primes(n):
    """
    Find the first n prime numbers using a for loop.

    Args:
        n (int): Number of primes to find

    Returns:
        list: List of first n prime numbers
    """
    primes = []
    num = 2

    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1

    print(f"First {n} prime numbers: {primes}")
    return primes

def sum_1_to_n(n):
    """
    Find the sum of all numbers from 1 to n using a while loop.

    Args:
        n (int): The upper limit

    Returns:
        int: Sum of numbers from 1 to n
    """
    total = 0
    current = 1

    while current <= n:
        total += current
        current += 1

    print(f"Sum of numbers from 1 to {n}: {total}")
    return total

if __name__ == "__main__":
    check_number_sign(5)
    check_number_sign(-3)
    check_number_sign(0)

    first_n_primes(10)

    sum_1_to_n(100)
