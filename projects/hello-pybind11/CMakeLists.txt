cmake_minimum_required(VERSION 3.15...3.26)

project(hello-pybind11 VERSION "0.1")

# Define CMAKE_INSTALL_xxx: LIBDIR, INCLUDEDIR
include(GNUInstallDirs)
include(FetchContent)

FetchContent_Declare(
  pybind11
  URL https://github.com/pybind/pybind11/archive/refs/tags/v2.13.6.tar.gz
  URL_HASH SHA256=e08cb87f4773da97fa7b5f035de8763abc656d87d5773e62f6da0587d1f0ec20
)
FetchContent_MakeAvailable(pybind11)

set(python_module_name _hello)
pybind11_add_module(${python_module_name} MODULE
  src/hello/hello_py.cpp
)

install(TARGETS ${python_module_name} DESTINATION .)
