
message(STATUS "F2PY_INCLUDE_DIR:${F2PY_INCLUDE_DIR}")
message(STATUS "NumPy_INCLUDE_DIR:${NumPy_INCLUDE_DIR}")

set(f2py_module_name "cylinder_methods")
set(fortran_src_file "${PROJECT_SOURCE_DIR}/src/cylinder_methods.f90")

set(generated_src_file ${CMAKE_CURRENT_BINARY_DIR}/${f2py_module_name}module.c)

add_custom_command(
  OUTPUT ${generated_src_file}
  COMMAND ${F2PY_EXECUTABLE}
    -m ${f2py_module_name}
    ${fortran_src_file}
  WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
  )

set(module_name _${f2py_module_name})

add_library(${module_name} MODULE ${generated_src_file})
python_extension_module(${module_name})
target_include_directories(${module_name} PRIVATE ${F2PY_INCLUDE_DIR} ${NumPy_INCLUDE_DIR})
install(TARGETS ${module_name} LIBRARY DESTINATION hello)
