"""Tests for the Fibonacci extension."""

import pytest
from fibonacci import fibonacci, fibonacci_sequence


class TestFibonacci:
    """Test cases for fibonacci() function."""

    def test_fibonacci_zero(self):
        """Test Fibonacci of 0."""
        assert fibonacci(0) == 0

    def test_fibonacci_one(self):
        """Test Fibonacci of 1."""
        assert fibonacci(1) == 1

    def test_fibonacci_basic_sequence(self):
        """Test basic Fibonacci sequence values."""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        for i, expected_val in enumerate(expected):
            assert fibonacci(i) == expected_val, f"fibonacci({i}) should be {expected_val}"

    def test_fibonacci_larger_values(self):
        """Test larger Fibonacci numbers."""
        assert fibonacci(20) == 6765
        assert fibonacci(30) == 832040

    def test_fibonacci_negative_raises(self):
        """Test that negative n raises ValueError."""
        with pytest.raises(ValueError, match="n must be non-negative"):
            fibonacci(-1)

        with pytest.raises(ValueError, match="n must be non-negative"):
            fibonacci(-10)


class TestFibonacciSequence:
    """Test cases for fibonacci_sequence() function."""

    def test_sequence_empty(self):
        """Test generating 0 Fibonacci numbers."""
        assert fibonacci_sequence(0) == []

    def test_sequence_single(self):
        """Test generating 1 Fibonacci number."""
        assert fibonacci_sequence(1) == [0]

    def test_sequence_two(self):
        """Test generating 2 Fibonacci numbers."""
        assert fibonacci_sequence(2) == [0, 1]

    def test_sequence_basic(self):
        """Test generating basic Fibonacci sequence."""
        result = fibonacci_sequence(10)
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        assert result == expected

    def test_sequence_negative_raises(self):
        """Test that negative n raises ValueError."""
        with pytest.raises(ValueError, match="n must be non-negative"):
            fibonacci_sequence(-1)

        with pytest.raises(ValueError, match="n must be non-negative"):
            fibonacci_sequence(-5)

    def test_sequence_larger(self):
        """Test generating larger sequence."""
        result = fibonacci_sequence(15)
        assert len(result) == 15
        assert result[0] == 0
        assert result[1] == 1
        assert result[-1] == 377  # 15th Fibonacci number


class TestConsistency:
    """Test consistency between fibonacci and fibonacci_sequence."""

    def test_sequence_matches_fibonacci(self):
        """Test that fibonacci_sequence results match individual fibonacci calls."""
        n = 20
        sequence = fibonacci_sequence(n)
        for i, expected_val in enumerate(sequence):
            assert fibonacci(i) == expected_val, \
                f"fibonacci({i}) should match sequence[{i}]"
