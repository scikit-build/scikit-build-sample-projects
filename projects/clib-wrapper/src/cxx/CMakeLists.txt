set(MY_C_MODULE_NAME "my_c_module")

list(APPEND sources "my_c_module.c")

add_library(${MY_C_MODULE_NAME} SHARED ${sources})

file(RELATIVE_PATH install_dest "${CMAKE_SOURCE_DIR}" "${CMAKE_CURRENT_SOURCE_DIR}")
install(TARGETS ${MY_C_MODULE_NAME} LIBRARY DESTINATION "${install_dest}")
