# Pi

This is an example project demonstrating the use of scikit-build for distributing a standalone FORTRAN library, *pi*;
a CMake package for that library; and a Python wrapper implemented in f2py.

The example assume some familiarity with CMake and f2py, only really going into detail on the scikit-build parts.

To install the package run in the project directory

```bash
pip install .
```

To run the Python tests, first install the package, then in the project directory run

```bash
pytest
```
