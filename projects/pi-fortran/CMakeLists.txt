cmake_minimum_required(VERSION 3.4...3.22)

project(pi)

find_package(PythonInterp REQUIRED)
find_package(PythonLibs)
find_package(PythonExtensions REQUIRED)

# F2PY headers
execute_process(
  COMMAND "${PYTHON_EXECUTABLE}"
  -c "import numpy.f2py; print(numpy.f2py.get_include())"
  OUTPUT_VARIABLE F2PY_INCLUDE_DIR
  OUTPUT_STRIP_TRAILING_WHITESPACE
)
find_package(F2PY REQUIRED)

add_f2py_target(pi pi/_pi.f)

add_library(pi MODULE ${pi})
target_link_libraries(pi)
install(TARGETS pi DESTINATION .)
