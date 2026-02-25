"""Example usage of the Fibonacci extension."""

from fibonacci import fibonacci, fibonacci_sequence


def main():
    """Demonstrate Fibonacci extension functionality."""
    print("=" * 50)
    print("Fibonacci Extension Demo")
    print("=" * 50)

    # Calculate single Fibonacci numbers
    print("\nSingle Fibonacci calculations:")
    for i in range(1, 11):
        result = fibonacci(i)
        print(f"  fibonacci({i}) = {result}")

    # Generate Fibonacci sequence
    print("\nFirst 10 Fibonacci numbers:")
    sequence = fibonacci_sequence(10)
    print(f"  {sequence}")

    # Larger calculation
    print("\nLarger Fibonacci numbers:")
    large_n = 50
    result = fibonacci(large_n)
    print(f"  fibonacci({large_n}) = {result}")


if __name__ == "__main__":
    main()
