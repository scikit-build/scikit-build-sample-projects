cmake_minimum_required(VERSION 3.15...3.29)

project(${SKBUILD_PROJECT_NAME} VERSION ${SKBUILD_PROJECT_VERSION} LANGUAGES CXX)

set(PYBIND11_FINDPYTHON ON)
find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(_core MODULE cpp/_core.cpp)

install(TARGETS _core  DESTINATION skcdemo)
