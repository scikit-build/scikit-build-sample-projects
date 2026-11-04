cmake_minimum_required(VERSION 3.24...4.3)

# Conan's profile detection expects a C compiler as well.
project(${SKBUILD_PROJECT_NAME} VERSION ${SKBUILD_PROJECT_VERSION} LANGUAGES C CXX)

find_package(Python 3.11 REQUIRED COMPONENTS Interpreter Development.Module)
find_package(pybind11 CONFIG REQUIRED)
# Provided by Conan through conan_provider.cmake
find_package(fmt CONFIG REQUIRED)

pybind11_add_module(conan_hello MODULE conan_hello.cpp)
target_link_libraries(conan_hello PRIVATE fmt::fmt)

install(TARGETS conan_hello DESTINATION .)
