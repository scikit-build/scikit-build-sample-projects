cmake_minimum_required(VERSION 3.15...3.26)

project(hello_cython)

find_package(PythonExtensions REQUIRED)
find_package(Cython REQUIRED)

add_subdirectory(hello)
