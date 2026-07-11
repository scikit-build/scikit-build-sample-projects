cmake_minimum_required(VERSION 3.15...4.4)

project(${SKBUILD_PROJECT_NAME} VERSION ${SKBUILD_PROJECT_VERSION} LANGUAGES C)

find_package(Python REQUIRED COMPONENTS Interpreter Development.Module
                                        ${SKBUILD_SABI_COMPONENT})

set(HELLO_CDEF "${CMAKE_CURRENT_SOURCE_DIR}/src/hello/_hello.cdef.txt")
set(HELLO_CSRC "${CMAKE_CURRENT_SOURCE_DIR}/src/hello/_hello.csrc.c")
add_custom_command(
  OUTPUT _hello.c
  COMMAND Python::Interpreter -m cffi.gen_src read-sources hello._hello
          "${HELLO_CDEF}" "${HELLO_CSRC}" _hello.c
  DEPENDS "${HELLO_CDEF}" "${HELLO_CSRC}"
  VERBATIM)

# cffi's generated code targets the limited API unless
# _CFFI_NO_LIMITED_API is defined (or unavailable, like on 3.14t)
if(NOT "${SKBUILD_SABI_COMPONENT}" STREQUAL "")
  python_add_library(_hello MODULE USE_SABI "${SKBUILD_SABI_VERSION}" WITH_SOABI
                     "${CMAKE_CURRENT_BINARY_DIR}/_hello.c" csrc/square.c)
else()
  python_add_library(_hello MODULE WITH_SOABI
                     "${CMAKE_CURRENT_BINARY_DIR}/_hello.c" csrc/square.c)
endif()
target_include_directories(_hello PRIVATE csrc)

install(TARGETS _hello DESTINATION hello)
