cmake_minimum_required(VERSION 3.15...3.26)

project(${SKBUILD_PROJECT_NAME} VERSION ${SKBUILD_PROJECT_VERSION} LANGUAGES C)

find_package(Python REQUIRED COMPONENTS Interpreter Development.Module)

Python_add_library(skcdpure MODULE WITH_SOABI skcdpure.c)

install(TARGETS skcdpure DESTINATION .)
