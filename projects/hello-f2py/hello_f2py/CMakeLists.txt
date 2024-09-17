add_f2py_target(_hello _hello.pyf)
add_library(_hello MODULE ${_hello} hello.f90)
target_link_libraries(_hello ${F2PY_LIBRARIES})
target_include_directories(_hello PRIVATE ${F2PY_INCLUDE_DIRS})
python_extension_module(_hello)

install(TARGETS _hello LIBRARY DESTINATION hello_f2py)
