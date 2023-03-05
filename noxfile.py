import sys

import nox

hello_list = ["hello-pure", "hello-cpp", "hello-pybind11", "hello-cython"]
if not sys.platform.startswith("win"):
    hello_list.extend(["hello-cmake-package", "pi-fortran"])
long_hello_list = [*hello_list, "pen2-cython", "core-c-hello", "core-pybind11-hello"]


@nox.session
@nox.parametrize("module", long_hello_list, ids=long_hello_list)
def dist(session: nox.Session, module: str) -> None:
    session.cd(f"projects/{module}")
    session.install("build")

    # Builds SDist and wheel
    session.run("python", "-m", "build")


@nox.session
@nox.parametrize("module", hello_list, ids=hello_list)
def test(session: nox.Session, module: str) -> None:
    session.cd(f"projects/{module}")
    session.install("pytest", "pytest-cov")

    session.install(".")
    session.run("pytest")
