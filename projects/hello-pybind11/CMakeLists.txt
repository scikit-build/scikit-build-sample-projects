cmake_minimum_required(VERSION 3.4.0)

project(hello-pybind11)
set(HELLO_VERSION "0.1")

option(HELLO_BUILD_TESTING "Enable testing for this project" OFF)
option(HELLO_USE_SYSTEM_PYBIND11 "Use pybind11 installed in the system" OFF)
mark_as_advanced(HELLO_USE_SYSTEM_PYBIND11)

# To use cmake modules/functions or FindXXX files:
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/cmake")
include(GNUInstallDirs) # Define CMAKE_INSTALL_xxx: LIBDIR, INCLUDEDIR
set(hello_export_file "${PROJECT_BINARY_DIR}/helloTargets.cmake")

if(NOT HELLO_USE_SYSTEM_PYBIND11)
  # Fetch pybind11
  include(FetchContent)
  FetchContent_Declare(
    pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11
    GIT_TAG v2.3
  )
  FetchContent_GetProperties(pybind11)
  if(NOT pybind11_POPULATED)
    FetchContent_Populate(pybind11)
    add_subdirectory(${pybind11_SOURCE_DIR} ${pybind11_BINARY_DIR})
  endif()
else()
    find_package(pybind11 REQUIRED)
endif()

if(HELLO_BUILD_TESTING)
    enable_testing()
endif()

add_subdirectory(src)
add_subdirectory(wrap)

# Install/package
set(install_cmake_dir "${CMAKE_INSTALL_LIBDIR}/cmake/hello")
install (EXPORT helloTargets
  NAMESPACE hello::
  DESTINATION ${install_cmake_dir} )

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/cmake/helloConfig.cmake
              ${CMAKE_CURRENT_BINARY_DIR}/helloConfigVersion.cmake
              DESTINATION ${install_cmake_dir} )

include(CMakePackageConfigHelpers)

write_basic_package_version_file(helloConfigVersion.cmake
  VERSION ${HELLO_VERSION}
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

