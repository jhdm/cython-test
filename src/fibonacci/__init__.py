"""
Fibonacci extension - Fast Fibonacci number calculations using Cython.
"""

__version__ = "0.1.0"

try:
    from ._fibonacci import fibonacci, fibonacci_sequence
except ImportError:
    # Fallback for if the Cython extension isn't compiled
    import warnings
    warnings.warn("Cython extension not found, using pure Python fallback")

    def fibonacci(n):
        """Pure Python fallback for Fibonacci calculation."""
        if n < 0:
            raise ValueError("n must be non-negative")
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def fibonacci_sequence(n):
        """Pure Python fallback for Fibonacci sequence generation."""
        if n < 0:
            raise ValueError("n must be non-negative")
        if n == 0:
            return []
        sequence = [0]
        if n == 1:
            return sequence
        sequence.append(1)
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
            sequence.append(b)
        return sequence

__all__ = ["fibonacci", "fibonacci_sequence"]
