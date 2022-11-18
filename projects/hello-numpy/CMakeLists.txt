cmake_minimum_required(VERSION 3.18...3.22)

project(hello-numpy VERSION "0.1")

# Define CMAKE_INSTALL_xxx: LIBDIR, INCLUDEDIR
include(GNUInstallDirs)

find_package(Python COMPONENTS Interpreter Development.Module NumPy)

find_package(pybind11 CONFIG REQUIRED)

set(python_module_name _hello)
pybind11_add_module(${python_module_name} MODULE
    src/hello/hello_py.cpp
)
target_link_libraries(${python_module_name} PRIVATE Python::NumPy)

install(TARGETS ${python_module_name} DESTINATION .)

# Quiet a warning, since this project is only valid with SKBUILD
set(ignoreMe "${SKBUILD}")
