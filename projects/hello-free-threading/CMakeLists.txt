cmake_minimum_required(VERSION 3.15...3.29)

project(FreeComputePi LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17 CACHE STRING "The C++ standard to use")
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(
  Python
  COMPONENTS Interpreter Development.Module
  REQUIRED)

python_add_library(_core MODULE src/freecomputepi/_core.cpp WITH_SOABI)

find_package(pybind11 REQUIRED)
pybind11_add_module(_pybcore MODULE src/freecomputepi/_pybcore.cpp)

install(TARGETS _core _pybcore DESTINATION freecomputepi)
