cmake_minimum_required(VERSION 3.15...4.3)

project(${SKBUILD_PROJECT_NAME} VERSION ${SKBUILD_PROJECT_VERSION} LANGUAGES C)

find_package(Python REQUIRED COMPONENTS Interpreter Development.Module)

add_custom_command(
  OUTPUT _hello.c
  COMMAND Python::Interpreter -m cffi.gen_src exec-python
          "${CMAKE_CURRENT_SOURCE_DIR}/src/hello/_hello_build.py" _hello.c
  DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/src/hello/_hello_build.py"
  VERBATIM)

python_add_library(_hello MODULE WITH_SOABI
                   "${CMAKE_CURRENT_BINARY_DIR}/_hello.c" csrc/square.c)
target_include_directories(_hello PRIVATE csrc)

install(TARGETS _hello DESTINATION hello)
