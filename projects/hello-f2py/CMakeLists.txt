cmake_minimum_required(VERSION 3.5.0)

project(hello_f2py)

find_package(PythonInterp REQUIRED)
find_package(PythonLibs)
find_package(PythonExtensions REQUIRED)
find_package(F2PY REQUIRED)

add_subdirectory(hello)
add_subdirectory(hello_auto)
