import sys

try:
    from skbuild import setup
except ImportError:
    print('scikit-build is required to build from source.', file=sys.stderr)
    print('Please run:', file=sys.stderr)
    print('', file=sys.stderr)
    print('  python -m pip install scikit-build')
    sys.exit(1)

setup(
    name="hello-pybind11",
    version="1.2.3",
    description="a minimal example package (with pybind11)",
    author='Pablo Hernandez-Cerdan',
    license="MIT",
    packages=['hello'],
    #cmake=['-DHELLO_BUILD_TESTING:BOOL=TRUE',]
)
