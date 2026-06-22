# Agent instructions

## What this repo is

A collection of small, self-contained example packages under `projects/`, each demonstrating how to build a Python extension with CMake. They serve as reference/test cases for the scikit-build ecosystem. There is no shared top-level package — each project builds and tests independently.

## Two generations of build backend

Projects fall into distinct families; know which one you're editing before changing build config:

- **Legacy `scikit-build`** (`build-backend = "setuptools.build_meta"`, has `setup.py`): `hello-pure`, `hello-cpp`, `hello-cython`, `hello-pybind11`, `pen2-cython`, `tower-of-babel`. Build requires include `scikit-build`, `cmake`, `ninja` in `[build-system].requires`. Metadata lives in `setup.py`.
- **Modern `scikit-build-core`** (`build-backend = "scikit_build_core.build"`, pyproject-only, no `setup.py`): `core-c-hello`, `core-pybind11-hello`, `hello-free-threading`, `pi-fortran`, `hello-cmake-package`. Metadata lives in `[project]`; configure via `[tool.scikit-build]`.
- **Hatchling + scikit-build-core plugin** (`build-backend = "hatchling.build"`): `hatchling-pybind11-hello`, using `[tool.hatch.build.targets.wheel.hooks.scikit-build]`.

Language bindings vary per project: pure Python, raw C/C++, pybind11, Cython, Fortran (`pi-fortran`). `tower-of-babel` is the broadest, exercising Boost + Cython static/shared linkage.

## Commands

Development is driven by nox (`noxfile.py`). Use `uvx nox` (uv is the assumed runner).

- Run all tests: `uvx nox -s test`
- Test a single project: `uvx nox -s "test(hello-cpp)"`
- Build sdist + wheel for all dist projects: `uvx nox -s dist`
- Build a single project's dists: `uvx nox -s "dist(hello-pybind11)"`
- Lint: `prek -a` (ruff + ruff-format + codespell, configured in `.pre-commit-config.yaml` / `ruff.toml`)

`nox -s test` installs the project and runs `pytest` inside `projects/<module>/`. To debug one project directly, `cd projects/<module>` and run `pip install .` then `pytest`.

## noxfile module lists (the source of truth for what gets built/tested)

`noxfile.py` defines which projects participate, with platform/version gates that must be respected when adding or moving a project:

- `hello_list` (tested by `test`): the four `hello-*` setuptools projects, plus `hello-cmake-package` and `pi-fortran` (**non-Windows only**), plus `hello-free-threading` (**Python 3.13+ only**).
- `long_hello_list` (built by `dist`): `hello_list` plus `pen2-cython`, `core-c-hello`, `core-pybind11-hello`, `hatchling-pybind11-hello`.
- `hello-free-threading` is wheel-built separately via cibuildwheel in CI (`free-threading` job), not through nox.

A new project is invisible to CI until added to the appropriate list here.

## Conventions

- Minimum Python is 3.9; ruff `target-version = "py39"`, line length 88.
- CI (`.github/workflows/ci.yml`) runs `dist` and `test` on ubuntu / macos-13 / windows via `uvx nox`. Fortran toolchain is set up on non-Windows runners.
- Untracked build outputs (`build/`, `_skbuild/`, `*.egg-info/`, generated `include/`/`share/` dirs, `uv.lock`) are byproducts — don't commit them.
