add_custom_command(
  OUTPUT _hello.c
  DEPENDS _hello.pyx
  COMMAND "${CYTHON}"
    "${CMAKE_CURRENT_SOURCE_DIR}/_hello.pyx"
    --output-file "${CMAKE_CURRENT_BINARY_DIR}/_hello.c"
  VERBATIM
  )

Python_add_library(_hello
  MODULE "${CMAKE_CURRENT_BINARY_DIR}/_hello.c"
  WITH_SOABI)

install(TARGETS _hello LIBRARY DESTINATION ${SKBUILD_PROJECT_NAME})
