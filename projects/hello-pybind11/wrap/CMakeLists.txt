# skbuild cmake macros not needed
# We'll use pybind11 functions to create and link libraries
# find_package(PythonExtensions REQUIRED)

set(python_module_name _hello)
pybind11_add_module(${python_module_name} MODULE
  hello_init_py.cpp
  hello_py.cpp
  )
target_link_libraries(${python_module_name} PRIVATE hellocore)

install(TARGETS ${python_module_name} DESTINATION hello)

# build tree
file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/__init__.py
     DESTINATION ${CMAKE_CURRENT_BINARY_DIR})
# install tree
install(FILES __init__.py DESTINATION hello)

# tests
if(HELLO_BUILD_TESTING)
  set(test_folder "${CMAKE_CURRENT_SOURCE_DIR}/test_python")
  set(python_tests_
    test_hello_pybind11.py
  )

  # test files should start with "test_"
  # unittest functions (in .py) should start with "test_" for discover to work
  foreach(python_test ${python_tests_})
      add_test(NAME python||${python_module_name}||${python_test}
        COMMAND ${PYTHON_EXECUTABLE}
          -m unittest discover
          -s ${test_folder}
          -p ${python_test}
      )
  endforeach()
endif()

