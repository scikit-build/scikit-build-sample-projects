cmake_minimum_required(VERSION 3.5...3.22)

project(hello LANGUAGES C Fortran)

find_package(PythonExtensions REQUIRED)
find_package(NumPy REQUIRED)
find_package(F2PY REQUIRED)

add_subdirectory(hello_f2py)
