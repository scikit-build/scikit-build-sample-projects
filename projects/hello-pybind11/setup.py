from skbuild import setup

setup(
    name="hello-pybind11",
    version="1.2.3",
    description="a minimal example package (with pybind11)",
    author="Pablo Hernandez-Cerdan",
    license="MIT",
    packages=["hello"],
    package_dir={"": "src"},
    cmake_install_dir="src/hello",
    python_requires=">=3.7",
)
