import shutil
import sys

import nox

nox.needs_version = ">=2024.4.15"
nox.options.default_venv_backend = "uv|virtualenv"


def _fortran_env(module: str) -> dict[str, str] | None:
    """Build environment for a module, if it needs special handling.

    The Windows runners preset CMAKE_GENERATOR to Visual Studio, which has no
    Fortran support, so pi-fortran must use Ninja with the MinGW compilers (put
    on PATH by the CI workflow). Returns None when no overrides are needed.
    """
    if module != "pi-fortran" or not sys.platform.startswith("win"):
        return None
    gcc = shutil.which("gcc")
    gfortran = shutil.which("gfortran")
    if not (gcc and gfortran):
        return None
    # Forward slashes: backslashes would be read as escapes in CMAKE_ARGS.
    gcc = gcc.replace("\\", "/")
    gfortran = gfortran.replace("\\", "/")
    return {
        "CMAKE_GENERATOR": "Ninja",
        "CMAKE_ARGS": f"-DCMAKE_C_COMPILER={gcc} -DCMAKE_Fortran_COMPILER={gfortran}",
    }


hello_list = [
    "hello-pure",
    "hello-cpp",
    "hello-pybind11",
    "hello-cython",
    "hello-cmake-package",
    "pi-fortran",
]
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
    session.run("python", "-m", "build", *opt, env=_fortran_env(module))


@nox.session
@nox.parametrize("module", hello_list, ids=hello_list)
def test(session: nox.Session, module: str) -> None:
    session.cd(f"projects/{module}")
    session.install("pytest", "pytest-cov")

    session.install(".", env=_fortran_env(module))
    session.run("pytest")
