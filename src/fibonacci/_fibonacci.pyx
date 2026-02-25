# cython: language_level=3

"""
Cython implementation of Fibonacci calculation for optimal performance.
"""

def fibonacci(int n) -> long:
    """
    Calculate the nth Fibonacci number.

    Args:
        n: The position in the Fibonacci sequence (0-indexed)

    Returns:
        The nth Fibonacci number

    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0:
        return 0
    if n == 1:
        return 1

    cdef long a = <long>0, b = <long>1, c = <long>0

    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b


def fibonacci_sequence(int n) -> list[long]:
    """
    Generate a list of the first n Fibonacci numbers.

    Args:
        n: Number of Fibonacci numbers to generate

    Returns:
        List of the first n Fibonacci numbers

    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0:
        return []

    cdef list[long] sequence = [<long>0]

    if n == 1:
        return sequence

    sequence.append(<long>1)
    cdef long a = <long>0, b = <long>1, c = <long>0

    for _ in range(2, n):
        c = a + b
        sequence.append(c)
        a = b
        b = c

    return sequence
