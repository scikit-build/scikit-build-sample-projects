"""
Command to demonstrates the content of a built wheel

..code::bash

    python setup.py bdist_wheel
    unzip -l dist/my_python_package-1.0.0-*.whl

"""
from skbuild import setup

if __name__ == '__main__':
    setup(
        package_dir={'': 'src/python/'},
        name="my_python_package",
        version='1.0.0',
        packages=['my_python_package'],
    )
