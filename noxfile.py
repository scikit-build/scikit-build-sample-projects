import nox
from pathlib import Path
import shutil

hello_list = "hello-pure", "hello-cpp", "hello-pybind11", "hello-cython", "hello-cmake-package"


@nox.session
@nox.parametrize("module", hello_list + ("pen2-cython",))
def dist(session, module):
    session.cd(f"projects/{module}")
    session.install("build")

    # Cleanup bad caching
    skbuild = Path("_skbuild")
    if skbuild.exists():
        shutil.rmtree(skbuild)

    # Builds SDist and wheel
    session.run("pyproject-build")


@nox.session
@nox.parametrize("module", hello_list)
def test(session, module):
    session.cd(f"projects/{module}")
    session.install("pytest", "pytest-cov")

    # Cleanup bad caching
    skbuild = Path("_skbuild")
    if skbuild.exists():
        shutil.rmtree(skbuild)

    session.install(".")
    session.run("pytest")
