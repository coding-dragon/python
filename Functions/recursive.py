def factorial(n):
    """Calculate the factorial of a number recursively.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of the number n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Generate the nth Fibonacci number recursively.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Example usage:
factorial_of_5 = factorial(5)
print(f"The factorial of 5 is: {factorial_of_5}")

fibonacci_of_7 = fibonacci(7)
print(f"The 7th Fibonacci number is: {fibonacci_of_7}")