# Cython Example

A Python extension in Cython example.

## Requirements

* Python 3.8+
* Cython 0.29+
* setuptools 65+

## Quick Start

**Create virtual environment:**

```bash
uv venv --python 3.14
```

That will create virtual environment `.venv/` directory with Python 3.14.

**To install build dependencies:**

```bash
uv sync --group dev
```

**To build for development:**

```bash
uv run python setup.py build_ext --inplace
```

**To install current package in editable (development) mode:**

```bash
uv pip install -e .
```

**To try this package:**

```bash
uv run python -c 'from fibonacci import fibonacci; print(f"fibonacci(10): {fibonacci(10)}")'
```

**Expected Output:**

```txt
fibonacci(10): 55
```

### Example

```python
from fibonacci import fibonacci, fibonacci_sequence

# Calculate the nth Fibonacci number
result = fibonacci(10)  # Returns 55

# Generate sequence of first n Fibonacci numbers
sequence = fibonacci_sequence(10)  # Returns [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## To create setup.py

To create a setup.py file needed for build_ext:

```bash
uv run python -c "import setuptools; from Cython.Build import cythonize; import os; os.system('python setup.py build_ext --inplace')"
```

## Clean up

To clean up:

```bash
uv run python setup.py clean --all
rm -rf build/
rm -rf dist/
rm -rf *.egg-info/
rm -rf src/**/*.c
rm -rf src/**/*.so
rm -rf src/**/*.pyd
find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete 2>/dev/null || true
```
