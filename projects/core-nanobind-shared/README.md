# core-nanobind-shared

A minimal [scikit-build-core](https://scikit-build-core.readthedocs.io) +
[nanobind](https://nanobind.readthedocs.io) project where the extension module
links against a plain C++ **shared** library that ships inside the wheel.
Requested in
[scikit-build-core#1034](https://github.com/scikit-build/scikit-build-core/issues/1034).

## Layout

- `cpp/`: an ordinary C++ shared library (`say_hello`) with no Python
  knowledge. Stand-in for any existing `add_library(... SHARED ...)` target or
  third-party library you build yourself.
- `src/bindings.cpp`: the nanobind module `_hello`, which just links to the
  library with `target_link_libraries`.
- `src/hello/`: the pure Python package; scikit-build-core picks it up
  automatically because it matches the project name.

## The parts that trip people up

- **Install with relative destinations.** `install(TARGETS ... DESTINATION
  hello)` puts both binaries inside the `hello` package in the wheel. Never
  use `${CMAKE_INSTALL_PREFIX}` in destinations; scikit-build-core installs
  into a staging directory that becomes the wheel's platlib root.
- **RPATH.** At import time the extension must find the shared library next to
  itself, so its `INSTALL_RPATH` is set to `$ORIGIN` (Linux) or `@loader_path`
  (macOS). On macOS this works together with the default `@rpath/...` install
  name CMake gives shared libraries.
- **Windows.** There is no RPATH; the DLL is found because CPython loads
  extension modules with their own directory on the DLL search path, so
  installing the DLL next to the `.pyd` is enough (`RUNTIME DESTINATION`).
  The MSVC import library (`.lib`, the `ARCHIVE` artifact) is only needed at
  build time and is excluded from the wheel.
- **No `SOVERSION`/`VERSION` on the library.** Versioned shared libraries are
  installed as symlinks, but wheels cannot contain symlinks — you would ship
  multiple full copies of the library.

If you link against libraries you do *not* ship in the wheel, this RPATH setup
does not apply; use `auditwheel` (Linux) / `delocate` (macOS) /
`delvewheel` (Windows) to vendor them into repaired wheels instead.
