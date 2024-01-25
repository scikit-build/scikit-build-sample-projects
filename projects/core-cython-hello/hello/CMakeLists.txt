Cython_compile_pyx(_hello.pyx
  OUTPUT_VAR _hello_source_file
  )

Python_add_library(_hello
  MODULE ${_hello_source_file}
  WITH_SOABI)

install(TARGETS _hello LIBRARY DESTINATION ${SKBUILD_PROJECT_NAME})
