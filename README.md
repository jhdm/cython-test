# Fibonacci Extension

A high-performance Fibonacci calculation library built with Cython for use in other Python programs.

## Features

- ⚡ Fast Fibonacci calculation using Cython
- 🔧 Easy-to-use API with pure Python fallback
- 📦 Installable as a Python package
- 🛠️ Build automation with `just` task runner

## Installation

### From Source

1. Clone the repository
2. Install build dependencies:
   ```bash
   just dev-deps
   ```
3. Build and install:
   ```bash
   just setup
   ```

### For Development

Install in editable mode:
```bash
just dev
```

## Usage

### Basic Usage

```python
from fibonacci import fibonacci, fibonacci_sequence

# Calculate the nth Fibonacci number
result = fibonacci(10)  # Returns 55

# Generate sequence of first n Fibonacci numbers
sequence = fibonacci_sequence(10)  # Returns [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### In Your Package

Add this to your `pyproject.toml`:
```toml
[project]
dependencies = [
    "fibonacci-extension>=0.1.0",
]
```

Then in your code:
```python
from fibonacci import fibonacci

fib_number = fibonacci(100)
```

## Build Tasks

Use `just` to manage the project:

```bash
just setup          # Install dependencies and build extension
just dev            # Install in development mode
just dev-deps       # Install development dependencies
just build          # Build the Cython extension
just wheel          # Build wheel distribution
just sdist          # Build source distribution
just dist           # Build all distributions (wheel + sdist)
just clean          # Clean build artifacts
just test           # Run tests
just install-test   # Build and install for testing
just help           # Show all available tasks
```

## Requirements

- Python 3.8+
- Cython 0.29+
- setuptools 65+

## API Reference

### `fibonacci(n: int) -> int`

Calculate the nth Fibonacci number.

**Parameters:**
- `n` (int): Position in the Fibonacci sequence (0-indexed)

**Returns:**
- The nth Fibonacci number

**Raises:**
- `ValueError`: If n is negative

**Example:**
```python
from fibonacci import fibonacci
print(fibonacci(10))  # Output: 55
```

### `fibonacci_sequence(n: int) -> list`

Generate a list of the first n Fibonacci numbers.

**Parameters:**
- `n` (int): Number of Fibonacci numbers to generate

**Returns:**
- List of the first n Fibonacci numbers

**Raises:**
- `ValueError`: If n is negative

**Example:**
```python
from fibonacci import fibonacci_sequence
print(fibonacci_sequence(5))  # Output: [0, 1, 1, 2, 3]
```

## Example Script

Run the demo:
```bash
python main.py
```

## Performance

The Cython implementation provides significant performance improvements over pure Python for large calculations:

- Single calculation: ~100x faster for large n (n > 100)
- Sequence generation: ~50x faster

## Directory Structure

```
.
├── src/
│   └── fibonacci/
│       ├── __init__.py
│       └── _fibonacci.pyx
├── setup.py
├── pyproject.toml
├── Justfile
├── main.py
└── README.md
```

## License

MIT

## Development

This project uses:
- **Cython**: For performance-critical extension code
- **setuptools**: For building and packaging
- **just**: For task automation
