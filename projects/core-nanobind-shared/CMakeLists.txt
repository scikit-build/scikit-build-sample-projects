cmake_minimum_required(VERSION 3.15...3.30)

project(${SKBUILD_PROJECT_NAME} VERSION ${SKBUILD_PROJECT_VERSION} LANGUAGES CXX)

find_package(
  Python
  COMPONENTS Interpreter Development.Module
  REQUIRED)
find_package(nanobind CONFIG REQUIRED)

# An ordinary C++ shared library that knows nothing about Python. In a real
# project this could be a pre-existing library or an imported target.
add_library(say_hello SHARED cpp/hello.cpp)
target_include_directories(say_hello PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/cpp")
# MSVC exports nothing by default; real projects usually use
# generate_export_header() and explicit __declspec macros instead.
set_target_properties(say_hello PROPERTIES WINDOWS_EXPORT_ALL_SYMBOLS ON)

# The Python extension module, linked to the shared library like any other
# CMake consumer.
nanobind_add_module(_hello src/bindings.cpp)
target_link_libraries(_hello PRIVATE say_hello)

# Both binaries are installed side by side into the "hello" package, so the
# extension must look next to itself for the library at import time. Windows
# has no RPATH; there the DLL is found because it sits next to the .pyd.
if(APPLE)
  set_target_properties(_hello PROPERTIES INSTALL_RPATH "@loader_path")
elseif(UNIX)
  set_target_properties(_hello PROPERTIES INSTALL_RPATH "$ORIGIN")
endif()

# Destinations are relative to the root of the wheel (platlib). LIBRARY covers
# the extension and the .so/.dylib, RUNTIME covers the .dll on Windows, and
# the MSVC import library (ARCHIVE) is a build-time artifact that doesn't
# belong in the wheel.
install(
  TARGETS _hello say_hello
  LIBRARY DESTINATION hello
  RUNTIME DESTINATION hello
  ARCHIVE DESTINATION hello EXCLUDE_FROM_ALL)
