set(hello_sources
  hello.cpp
  )

add_library(hellocore ${hello_sources} )
target_include_directories(hellocore PUBLIC
  $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
  )

# Required for pybind11 when building STATIC libraries.
# It's ON by default with SHARED or MODULE libraries.
set_property(TARGET hellocore PROPERTY POSITION_INDEPENDENT_CODE ON)


# install targets
install(TARGETS hellocore
        EXPORT helloTargets
        RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
        )

install(DIRECTORY ${PROJECT_SOURCE_DIR}/include/
  DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/hello
  PATTERN "*.txt" EXCLUDE)

# export to the build tree
export( TARGETS hellocore
  NAMESPACE hello::
  APPEND FILE ${hello_export_file})

# Add the wrapper
add_subdirectory(hello)
