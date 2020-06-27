# skbuild cmake macros not needed
# We'll use pybind11 functions to create and link libraries
# find_package(PythonExtensions REQUIRED)

set(python_module_name _hello)
pybind11_add_module(${python_module_name} MODULE
  hello_py.cpp
  )
target_link_libraries(${python_module_name} PRIVATE hellocore)
if (APPLE)
  set(rpath "@loader_path")
else()
  set(rpath "$ORIGIN")
endif()
set_target_properties(${python_module_name} PROPERTIES
    INSTALL_RPATH ${rpath})

install(TARGETS ${python_module_name} DESTINATION src/hello)

# tests
if(BUILD_TESTING)
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

