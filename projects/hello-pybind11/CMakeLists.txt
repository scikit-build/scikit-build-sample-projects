cmake_minimum_required(VERSION 3.14...3.17)

project(hello-pybind11 VERSION "0.1")

option(HELLO_USE_SYSTEM_PYBIND11 "Use pybind11 installed in the system" OFF)

# Define CMAKE_INSTALL_xxx: LIBDIR, INCLUDEDIR
include(GNUInstallDirs)

# CMake files not included if installed via pyproject.toml, so manually doing it here.
if(NOT HELLO_USE_SYSTEM_PYBIND11)
  # Fetch pybind11
  include(FetchContent)

  FetchContent_Declare(
    pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11
    GIT_TAG v2.5.0
  )
  FetchContent_MakeAvailable(pybind11)

else()
  find_package(pybind11 REQUIRED)
endif()

set(python_module_name _hello)
pybind11_add_module(${python_module_name} MODULE
  src/hello/hello_py.cpp
  )

install(TARGETS ${python_module_name} DESTINATION src/hello)

# Quiet a warning, since this project is only valid with SKBUILD
set(ignoreMe "${SKBUILD}")
