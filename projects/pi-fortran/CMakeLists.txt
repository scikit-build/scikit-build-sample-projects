cmake_minimum_required(VERSION 3.17.2...3.29)

project(pi
  VERSION 1.0.1
  DESCRIPTION "pi estimator"
  LANGUAGES C Fortran
)

find_package(
  Python
  COMPONENTS Interpreter Development.Module NumPy
  REQUIRED)

include(UseF2Py)

# Build the extension in one call: f2py generates the wrappers from the
# checked-in signature file, then it and _pi.f are compiled and linked together
# with fortranobject. The module name (pi) is taken from the .pyf stem.
f2py_add_module(pi/pi.pyf pi/_pi.f)

# With the MinGW toolchain (Windows), statically link the GNU runtime so the
# module has no external libgfortran/libgcc/libwinpthread DLL dependencies.
if(WIN32 AND CMAKE_Fortran_COMPILER_ID STREQUAL "GNU")
  target_link_options(pi PRIVATE -static)
endif()

install(TARGETS pi DESTINATION pi)
