# skbuild cmake macros not needed
# We'll use pybind11 functions to create and link libraries
# find_package(PythonExtensions REQUIRED)

set(python_module_name _hello)
pybind11_add_module(${python_module_name} MODULE
  hello_py.cpp
  )

install(TARGETS ${python_module_name} DESTINATION src/hello)

