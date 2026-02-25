"""Type stubs for the Cython _fibonacci module."""

from Cython import long


def fibonacci(n: int) -> long:
    """
    Calculate the nth Fibonacci number.

    Args:
        n: The position in the Fibonacci sequence (0-indexed)

    Returns:
        The nth Fibonacci number

    Raises:
        ValueError: If n is negative
    """
    ...

def fibonacci_sequence(n: int) -> list[long]:
    """
    Generate a list of the first n Fibonacci numbers.

    Args:
        n: Number of Fibonacci numbers to generate

    Returns:
        List of the first n Fibonacci numbers

    Raises:
        ValueError: If n is negative
    """
    ...
