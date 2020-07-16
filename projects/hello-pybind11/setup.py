import sys

try:
    from skbuild import setup
except ImportError:
    print('Please update pip, you need pip 10 or greater,\n'
          ' or you need to install the PEP 518 requirements in pyproject.toml yourself', file=sys.stderr)
    raise

setup(
    name="hello-pybind11",
    version="1.2.3",
    description="a minimal example package (with pybind11)",
    author='Pablo Hernandez-Cerdan',
    license="MIT",
    packages=['hello'],
    package_dir={'': 'src'},
    cmake_install_dir='src/hello'
)
