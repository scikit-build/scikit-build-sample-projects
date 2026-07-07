"""CFFI builder script, executed by `cffi-gen-src exec-python` at build time.

This is the same script a setuptools cffi project would pass to
``cffi_modules=``; here it is only an input to the source generator.
"""

from cffi import FFI

ffibuilder = FFI()
ffibuilder.cdef("int square(int n);")
ffibuilder.set_source(
    "hello._hello",
    '#include "square.h"',
)
