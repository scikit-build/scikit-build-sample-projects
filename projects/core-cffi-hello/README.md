# core-cffi-hello

A minimal [scikit-build-core](https://scikit-build-core.readthedocs.io) +
[cffi](https://cffi.readthedocs.io) project that generates the extension
source at build time with the
[`cffi-gen-src`](https://cffi.readthedocs.io/en/stable/cffi-gen-src.html) CLI
(new in cffi 2.1). It is the scikit-build-core analog of the meson-python
example in the cffi documentation.

## Layout

- `csrc/`: a plain C library (`square.c`/`square.h`) with no Python or cffi
  knowledge.
- `src/hello/_hello.cdef.txt` and `src/hello/_hello.csrc.c`: the FFI
  definitions and the C source prelude, read by `cffi-gen-src read-sources`
  and turned into `_hello.c`. This replaces the classic builder script (an
  `FFI` object with `cdef()` and `set_source()`); if you already have one,
  the `exec-python` subcommand runs it directly instead.
- `src/hello/`: the pure Python package, picked up automatically because it
  matches the project name. `wheel.exclude` keeps the cdef/csrc build inputs
  out of the wheel.

## The parts that trip people up

- **Run the generator from CMake.** An `add_custom_command` invokes
  `python -m cffi.gen_src read-sources hello._hello <cdef> <csrc> _hello.c`
  (the module form of the `cffi-gen-src` script), so cffi from
  `[build-system].requires` is used. The generated file lands in the build
  tree and is compiled together with `csrc/square.c` by `python_add_library`.
  The module name (`hello._hello`) is a command-line argument here, not
  something read from a file — it must match where the extension is
  installed.
- **Compile/link flags move to CMake.** `cffi-gen-src` ignores the
  `libraries=`, `include_dirs=`, `library_dirs=`, and `extra_compile_args=`
  arguments of `set_source()`; use `target_include_directories`,
  `target_link_libraries`, etc. instead.
- **cffi is a runtime dependency.** The compiled module imports
  `_cffi_backend` when loaded, so `cffi` stays in `[project].dependencies`.
- **Python 3.10+.** cffi 2.1 is the first release shipping `cffi-gen-src`
  and requires Python 3.10, so `requires-python` (and the gate in the
  top-level `noxfile.py`) reflect that.
