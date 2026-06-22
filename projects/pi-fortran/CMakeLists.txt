cmake_minimum_required(VERSION 3.17.2...3.26)

project(pi
  VERSION 1.0.1
  DESCRIPTION "pi estimator"
  LANGUAGES C Fortran
)

find_package(Python REQUIRED COMPONENTS Interpreter Development.Module NumPy)

# F2PY headers
execute_process(
  COMMAND "${Python_EXECUTABLE}"
  -c "import numpy.f2py; print(numpy.f2py.get_include())"
  OUTPUT_VARIABLE F2PY_INCLUDE_DIR
  OUTPUT_STRIP_TRAILING_WHITESPACE
)
# On Windows the path comes back with backslashes, which CMake reads as escapes.
file(TO_CMAKE_PATH "${F2PY_INCLUDE_DIR}" F2PY_INCLUDE_DIR)

set(f2py_module_name "pi")
set(fortran_src_file "${CMAKE_SOURCE_DIR}/pi/_pi.f")
set(f2py_module_c "${f2py_module_name}module.c")

add_custom_command(
  OUTPUT "${CMAKE_CURRENT_BINARY_DIR}/${f2py_module_c}"
  COMMAND ${PYTHON_EXECUTABLE}  -m "numpy.f2py"
                   "${fortran_src_file}"
                   "${CMAKE_SOURCE_DIR}/pi/pi.pyf"  # Must include custom .pyf file
                   -m "pi"
                   --lower # Important
  DEPENDS pi/_pi.f # Fortran source
)

python_add_library(${CMAKE_PROJECT_NAME} MODULE
            "${f2py_module_name}module.c"
            "${F2PY_INCLUDE_DIR}/fortranobject.c"
            "${fortran_src_file}" WITH_SOABI)

target_include_directories(${CMAKE_PROJECT_NAME} PUBLIC
                           ${F2PY_INCLUDE_DIR}
                          )

target_link_libraries(${CMAKE_PROJECT_NAME} PUBLIC Python::NumPy)

# With the MinGW toolchain (Windows), statically link the GNU runtime so the
# module has no external libgfortran/libgcc/libwinpthread DLL dependencies.
if(WIN32 AND CMAKE_Fortran_COMPILER_ID STREQUAL "GNU")
  target_link_options(${CMAKE_PROJECT_NAME} PRIVATE -static)
endif()

install(TARGETS ${CMAKE_PROJECT_NAME} DESTINATION pi)
