cmake_minimum_required(VERSION 3.5...3.22)

project(hello LANGUAGES C Fortran)

find_package(PythonExtensions REQUIRED)
find_package(NumPy REQUIRED)
find_package(F2PY REQUIRED)

# see https://github.com/scikit-build/scikit-build/pull/495/
set_target_properties(_f2py_runtime_library PROPERTIES POSITION_INDEPENDENT_CODE ON)

add_subdirectory(hello_f2py)
