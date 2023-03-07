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

This is slightly modified from the example in the [numpy docs](https://numpy.org/devdocs/f2py/buildtools/skbuild.html), but we are using Monte Carlo to estimate the value of $\pi$.

A few surprises:
1. The dreaded underscore problem has a way of cropping up. One solution is explicitly writing out the interface in a [signature (`.pyf`) file](https://numpy.org/devdocs/f2py/signature-file.html).
2. The module will require numpy to work.
3. Between failed builds, it is best to clear out the `_skbuild` folder.
