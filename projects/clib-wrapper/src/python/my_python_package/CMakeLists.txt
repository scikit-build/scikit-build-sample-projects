set(cython_source "_cython_wrapper.pyx")
set(MODULE_NAME "_cython_wrapper")

# Translate Cython into C/C++
add_cython_target(${MODULE_NAME} "${cython_source}" C OUTPUT_VAR sources)

# Add other C sources
list(APPEND sources)

# Create C++ library. Specify include dirs and link libs as normal
add_library(${MODULE_NAME} MODULE ${sources})
target_include_directories(
  ${MODULE_NAME}
  PUBLIC
      ${NumPy_INCLUDE_DIRS}
      ${PYTHON_INCLUDE_DIR}
      ${CMAKE_CURRENT_SOURCE_DIR}
)

# TODO: not sure what the right way to do this is
set(MY_C_MODULE_NAME "my_c_module")

# What is the correct way to do this.
target_link_libraries(${MODULE_NAME} ${MY_C_MODULE_NAME})

target_compile_definitions(${MODULE_NAME} PUBLIC
  "NPY_NO_DEPRECATED_API"
  #"NPY_1_7_API_VERSION=0x00000007"
  )

python_extension_module(${MODULE_NAME})

file(RELATIVE_PATH install_dest "${CMAKE_SOURCE_DIR}" "${CMAKE_CURRENT_SOURCE_DIR}")
install(TARGETS ${MODULE_NAME} LIBRARY DESTINATION "${install_dest}")
