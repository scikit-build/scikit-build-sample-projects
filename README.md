# scikit-build sample projects

A collection of small, self-contained example packages demonstrating how to
build a Python extension with CMake using the
[scikit-build](https://github.com/scikit-build/scikit-build) ecosystem. Each
project under [`projects/`](projects/) builds and tests independently and serves
as a reference and test case for a particular language binding or build backend.

## Projects

The samples span two generations of build backend.

### Modern `scikit-build-core`

These are pyproject-only (no `setup.py`); metadata lives in `[project]` and is
configured via `[tool.scikit-build]`.

| Project | Demonstrates |
| --- | --- |
| [`core-c-hello`](projects/core-c-hello) | Raw C extension |
| [`core-cython-hello`](projects/core-cython-hello) | Cython via [cython-cmake](https://github.com/scikit-build/cython-cmake) |
| [`core-pybind11-hello`](projects/core-pybind11-hello) | pybind11 binding |
| [`hello-cmake-package`](projects/hello-cmake-package) | Standalone C library, exported CMake package, and pybind11 wrapper |
| [`hello-free-threading`](projects/hello-free-threading) | Free-threaded (no-GIL) build; requires Python 3.13+ |
| [`pi-fortran`](projects/pi-fortran) | Fortran via f2py and [f2py-cmake](https://github.com/scikit-build/f2py-cmake) |

### Hatchling + scikit-build-core plugin

| Project | Demonstrates |
| --- | --- |
| [`hatchling-pybind11-hello`](projects/hatchling-pybind11-hello) | pybind11 built through the [hatchling](https://hatch.pypa.io) plugin |

### Legacy `scikit-build`

These use `setuptools.build_meta` with a `setup.py`, and require `scikit-build`,
`cmake`, and `ninja` in `[build-system].requires`.

| Project | Demonstrates |
| --- | --- |
| [`hello-pure`](projects/hello-pure) | Pure Python (no compiled extension) |
| [`hello-cpp`](projects/hello-cpp) | Raw C++ extension |
| [`hello-cython`](projects/hello-cython) | Cython binding |
| [`hello-pybind11`](projects/hello-pybind11) | pybind11 binding |
| [`pen2-cython`](projects/pen2-cython) | Cython binding for a double-pendulum simulation |
| [`tower-of-babel`](projects/tower-of-babel) | The broadest example: Boost + Cython with static and shared linkage |

## Building and testing

Development is driven by [nox](https://nox.thea.codes), with
[uv](https://github.com/astral-sh/uv) as the assumed runner:

```bash
# Run all tests
uvx nox -s test

# Test a single project
uvx nox -s "test(hello-cpp)"

# Build sdist + wheel for all distributable projects
uvx nox -s dist

# Build a single project's dists
uvx nox -s "dist(hello-pybind11)"
```

To work with a single project directly, `cd` into it and use pip:

```bash
cd projects/hello-cpp
pip install .
pytest
```
