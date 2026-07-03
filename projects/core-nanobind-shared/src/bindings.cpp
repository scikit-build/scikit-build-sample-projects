#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>

#include "hello.hpp"

namespace nb = nanobind;

NB_MODULE(_hello, m) {
  m.doc() = "nanobind bindings for the say_hello shared library";
  m.def("add", &add, nb::arg("a"), nb::arg("b"), "Add two integers");
  m.def("greet", &greet, nb::arg("name"), "Greet somebody by name");
}
