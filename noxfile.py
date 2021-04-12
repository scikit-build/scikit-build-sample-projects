import nox


@nox.session
def hello_pure(session):
    session.cd("projects/hello-pure")
    session.install("pytest", "pytest-cov")
    session.install(".")
    session.run("pytest")

@nox.session
def hello_cpp(session):
    session.cd("projects/hello-cpp")
    session.install("pytest", "pytest-cov")
    session.install(".")
    session.cd("tests")
    session.run("pytest")

@nox.session
def hello_pybind11(session):
    session.cd("projects/hello-pybind11")
    session.install("pytest", "pytest-cov")
    session.install(".")
    session.run("pytest")

@nox.session
def hello_cython(session):
    session.cd("projects/hello-cython")
    session.install("pytest", "pytest-cov")
    session.install(".")
    session.cd("tests")
    session.run("pytest")

@nox.session
def pen2_cython(session):
    session.cd("projects/pen2-cython")
    session.install("build")
    session.run("pyproject-build")  # Builds SDist and wheel

