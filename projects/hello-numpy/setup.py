from skbuild import setup

setup(
    name="hello-numpy",
    version="1.2.3",
    description="a minimal example package (with pybind11 and NumPy)",
    author='Hameer Abbasi',
    license="MIT",
    packages=['hello'],
    package_dir={'': 'src'},
    cmake_install_dir='src/hello',
    python_requires='>=3.7',
)
