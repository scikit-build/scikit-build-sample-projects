import sys

import nox

nox.needs_version = ">=2024.4.15"
nox.options.default_venv_backend = "uv|virtualenv"

hello_list = ["hello-pure", "hello-cpp", "hello-pybind11", "hello-cython"]
if not sys.platform.startswith("win"):
    hello_list.extend(["hello-cmake-package", "pi-fortran"])
long_hello_list = [
    *hello_list,
    "pen2-cython",
    "core-c-hello",
    "core-pybind11-hello",
    "hatchling-pybind11-hello",
]
if sys.version_info >= (3, 13):
    hello_list.append("hello-free-threading")


@nox.session
@nox.parametrize("module", long_hello_list, ids=long_hello_list)
def dist(session: nox.Session, module: str) -> None:
    session.cd(f"projects/{module}")
    session.install("build")

    # Builds SDist and wheel
    opt = ["--installer=uv"] if session.venv_backend == "uv" else []
    session.run("python", "-m", "build", *opt)


@nox.session
@nox.parametrize("module", hello_list, ids=hello_list)
def test(session: nox.Session, module: str) -> None:
    session.cd(f"projects/{module}")
    session.install("pytest", "pytest-cov")

    session.install(".")
    session.run("pytest")
