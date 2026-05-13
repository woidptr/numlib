# Numerical Methods Library

A personal Python library implementing core numerical methods from scratch. This repository is built as a study tool to understand mathematical algorithms and to be used during exams.
**Note:** This package is intentionally not published to PyPI. It is meant to be installed directly from this Git repository into a local virtual environment.

## 📦 Installation

Since this library is not on PyPI, you can install it directly from GitHub using 'pip'.
Activate your virtual environment, then run:

```bash
pip install git+https://github.com/woidptr/numlib.git
```

## 🚀 Usage Examples

### 1. Root Finding (Bisection Method)**

```py
from numerical_methods.roots import bisection

# Define the function f(x) = x^2 - 4
my_func = lambda x: x**2 - 4.0

# Find the root between 0 and 5
root, iterations = bisection(func=my_func, a=0.0, b=5.0)
print(f"Root: {root} (found in {iterations} iterations)")
```
