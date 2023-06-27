cmake_minimum_required(VERSION 3.15...3.26)

project(
  hello
  VERSION "0.1.0"
  LANGUAGES CXX)

include(GNUInstallDirs)

# define the C++ library "hello"
add_library(hello SHARED "${PROJECT_SOURCE_DIR}/src/hello.cpp")

target_include_directories(
  hello PUBLIC $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
               $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>)

install(DIRECTORY "${PROJECT_SOURCE_DIR}/include/"
        DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

# Standard installation subdirs for the C++ library are used. The files will end
# up in the specified subdirectories under the Python package root. For example,
# "<python package prefix>/hello/lib/" if the destination is "lib/".
#
# Installing the objects in the package provides encapsulation and will become
# important later for binary redistribution reasons.
install(
  TARGETS hello
  EXPORT helloTargets
  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR})

# The CMake package config and target files are installed under the Python
# package root. This is necessary to ensure that all the relative paths in the
# helloTargets.cmake resolve correctly. It also provides encapsulation.
#
# The actual path used must be selected so that consuming projects can locate it
# via `find_package`. To support finding CMake packages in the Python package
# prefix, using `find_package`s default search path of
# `<prefix>/<name>/share/<name>*/cmake/` is reasonable. Adding the Python
# package installation prefix to CMAKE_PREFIX_PATH in combination with this path
# will allow `find_package` to find this package and any other package installed
# via a Python package if the CMake and Python packages are named the same.
set(HELLO_CMAKE_PACKAGE_INSTALL_SUBDIR "share/hello/cmake")

install(
  EXPORT helloTargets
  NAMESPACE hello::
  DESTINATION ${HELLO_CMAKE_PACKAGE_INSTALL_SUBDIR})

include(CMakePackageConfigHelpers)

write_basic_package_version_file(
  helloConfigVersion.cmake
  VERSION ${PROJECT_VERSION}
  COMPATIBILITY SameMinorVersion)

configure_package_config_file(
  "${PROJECT_SOURCE_DIR}/cmake/helloConfig.cmake.in" helloConfig.cmake
  INSTALL_DESTINATION ${HELLO_CMAKE_PACKAGE_INSTALL_SUBDIR})

install(FILES "${PROJECT_BINARY_DIR}/helloConfig.cmake"
              "${PROJECT_BINARY_DIR}/helloConfigVersion.cmake"
        DESTINATION ${HELLO_CMAKE_PACKAGE_INSTALL_SUBDIR})

# We are using the SKBUILD variable, which is defined when scikit-build is
# running the CMake build, to control building the Python wrapper. This allows
# the C++ project to be installed, standalone, when using the standard CMake
# build flow.
if(DEFINED SKBUILD)

  # call pybind11-config to obtain the root of the cmake package
  execute_process(COMMAND ${PYTHON_EXECUTABLE} -m pybind11 --cmakedir
                  OUTPUT_VARIABLE pybind11_ROOT_RAW)
  string(STRIP ${pybind11_ROOT_RAW} pybind11_ROOT)
  find_package(pybind11)

  pybind11_add_module(_hello MODULE
                      "${PROJECT_SOURCE_DIR}/src/hello/hello_py.cpp")

  target_link_libraries(_hello PRIVATE hello)

  # Installing the extension module to the root of the package
  install(TARGETS _hello DESTINATION .)

  configure_file("${PROJECT_SOURCE_DIR}/src/hello/__main__.py.in"
                 "${PROJECT_BINARY_DIR}/src/hello/__main__.py")

  install(FILES "${PROJECT_BINARY_DIR}/src/hello/__main__.py" DESTINATION .)

  # The extension module must load the hello library as a dependency when the
  # extension module is loaded. The easiest way to locate the hello library is
  # via RPATH. Absolute RPATHs are possible, but they make the resulting
  # binaries not redistributable to other Python installations (conda is broke,
  # wheel reuse is broke, and more!).
  #
  # Placing the hello library in the package and using relative RPATHs that
  # doesn't point outside of the package means that the built package is
  # relocatable. This allows for safe binary redistribution.
  if(APPLE)
    set_target_properties(
      _hello PROPERTIES INSTALL_RPATH "@loader_path/${CMAKE_INSTALL_LIBDIR}")
  else()
    set_target_properties(_hello PROPERTIES INSTALL_RPATH
                                            "$ORIGIN/${CMAKE_INSTALL_LIBDIR}")
  endif()

endif()
