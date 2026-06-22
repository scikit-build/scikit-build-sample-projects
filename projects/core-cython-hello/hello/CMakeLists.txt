cython_transpile(_hello.pyx LANGUAGE C OUTPUT_VARIABLE _hello_c)

python_add_library(_hello MODULE "${_hello_c}" WITH_SOABI)

install(TARGETS _hello LIBRARY DESTINATION ${SKBUILD_PROJECT_NAME})
