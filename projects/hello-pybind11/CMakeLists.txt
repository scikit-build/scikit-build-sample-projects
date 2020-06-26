cmake_minimum_required(VERSION 3.14...3.17)

project(hello-pybind11 VERSION "0.1")

include(CTest)
option(BUILD_TESTING "Build the tests too" OFF) # defined above, but on by default
option(HELLO_USE_SYSTEM_PYBIND11 "Use pybind11 installed in the system" OFF)

# Define CMAKE_INSTALL_xxx: LIBDIR, INCLUDEDIR
include(GNUInstallDirs)

# To use cmake modules/functions or FindXXX files:
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/cmake")
set(hello_export_file "${PROJECT_BINARY_DIR}/helloTargets.cmake")

# CMake files not included if installed via pyproject.toml, so manually doing it here.
if(NOT HELLO_USE_SYSTEM_PYBIND11)
  # Fetch pybind11
  include(FetchContent)

  FetchContent_Declare(
    pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11
    GIT_TAG v2.5.0
  )
  FetchContent_MakeAvailable(pybind11)

else()
  find_package(pybind11 REQUIRED)
endif()


add_subdirectory(src)

# Quiet a warning, since this project is only valid with SKBUILD
set(ignoreMe "${SKBUILD}")

# Everything below here is optional
# This installs CMake config tools
# And also a version file - which is not used by Python.


set(install_cmake_dir "${CMAKE_INSTALL_LIBDIR}/cmake/hello")
install (EXPORT helloTargets
  NAMESPACE hello::
  DESTINATION ${install_cmake_dir} )

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/cmake/helloConfig.cmake
              ${CMAKE_CURRENT_BINARY_DIR}/helloConfigVersion.cmake
              DESTINATION ${install_cmake_dir} )

include(CMakePackageConfigHelpers)

write_basic_package_version_file(helloConfigVersion.cmake
  VERSION ${PACKAGE_VERSION}
  COMPATIBILITY SameMajorVersion)

# Build tree
set(HELLO_TARGETS_FILE ${hello_export_file})
configure_package_config_file(
  ${CMAKE_CURRENT_SOURCE_DIR}/cmake/helloConfig.cmake.in
  ${CMAKE_CURRENT_BINARY_DIR}/helloConfig.cmake
  INSTALL_DESTINATION ${install_cmake_dir}
  PATH_VARS HELLO_TARGETS_FILE
  NO_CHECK_REQUIRED_COMPONENTS_MACRO # hello does not provide components
  INSTALL_PREFIX ${CMAKE_CURRENT_BINARY_DIR}
  )

# Install tree
set(HELLO_TARGETS_FILE ${CMAKE_INSTALL_PREFIX}/${install_cmake_dir}/helloTargets.cmake)
configure_package_config_file(
  ${CMAKE_CURRENT_SOURCE_DIR}/cmake/helloConfig.cmake.in
  ${CMAKE_CURRENT_BINARY_DIR}/cmake/helloConfig.cmake
  INSTALL_DESTINATION ${install_cmake_dir}
  PATH_VARS HELLO_TARGETS_FILE
  NO_CHECK_REQUIRED_COMPONENTS_MACRO # hello does not provide components
  )

