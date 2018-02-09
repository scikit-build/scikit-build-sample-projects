from skbuild import setup

setup(
    name="hello-cpp",
    version="1.2.3",
    description="a minimal example package (f2py version)",
    author='The scikit-build team',
    license="MIT",
    packages=['hello', 'hello_auto'],
)
