from skbuild import setup

setup(
    name="pi-fortran",
    version="1.0.1",
    description="a minimal example package (fortran version)",
    author="The scikit-build team",
    license="MIT",
    packages=["pi"],
    python_requires=">=3.7",
    install_requires=["numpy>=1.21"],
)
