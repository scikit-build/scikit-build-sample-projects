add_f2py_target(_hello _hello.pyf hello.f90)
add_library(_hello MODULE ${_hello})
python_extension_module(_hello)

target_link_libraries(_hello ${F2PY_LIBRARIES})
target_include_directories(_hello PRIVATE ${F2PY_INCLUDE_DIRS})

install(TARGETS _hello LIBRARY DESTINATION hello)
