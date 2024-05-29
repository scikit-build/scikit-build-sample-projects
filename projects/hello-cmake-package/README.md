# Hello

This is an example project demonstrating the use of scikit-build for distributing a standalone C library, *hello*;
a CMake package for that library; and a Python wrapper implemented in pybind11.

The example assume some familiarity with CMake and pybind11, only really going into detail on the scikit-build parts.
pybind11 is used to implement the binding, but anything is possible: swig, C API library, etc.

To install the package run in the project directory

```bash
pip install .
```

To run the Python tests, first install the package then in the project directory run

```bash
pytest
```

To run the C++ test, first install the package, then configure and build the project

```bash
cmake -S test/cpp -B build/ -Dhello_ROOT=$(python -m hello --cmakefiles)
cmake --build build/
```

Then run ctest in the build dir

```bash
cd build/
ctest
```
