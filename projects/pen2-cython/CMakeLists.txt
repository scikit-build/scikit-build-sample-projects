cmake_minimum_required(VERSION 3.15...3.26)

project(pen2_cython)

enable_testing()

find_package(PythonExtensions REQUIRED)
find_package(Cython REQUIRED)

add_subdirectory(src)
add_subdirectory(scripts)
