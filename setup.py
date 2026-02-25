"""Setup configuration for Fibonacci Cython extension."""

from setuptools import setup, Extension
from Cython.Build import cythonize
import os

# Define the extension module
ext_modules = [
    Extension(
        "fibonacci._fibonacci",
        sources=["src/fibonacci/_fibonacci.pyx"],
        language="c",
    )
]

# Build extensions
extensions = cythonize(ext_modules, language_level=3)

setup(
    ext_modules=extensions,
    package_dir={"": "src"},
    packages=["fibonacci"],
)
