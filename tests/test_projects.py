
from . import project_test, run_setup


@project_test("hello-cpp")
def test_hello_cpp(virtualenv):
    run_setup(virtualenv, ["test", "sdist", "bdist_wheel"])


@project_test("hello-cython")
def test_hello_cython(virtualenv):
    run_setup(virtualenv, ["test", "sdist", "bdist_wheel"])


@project_test("hello-pure")
def test_hello_pure(virtualenv):
    run_setup(virtualenv, ["test", "sdist", "bdist_wheel"])


@project_test("pen2-cython")
def test_pen2_cython(virtualenv):
    run_setup(virtualenv, ["sdist", "bdist_wheel"])
