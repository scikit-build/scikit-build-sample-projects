#include <pybind11/pybind11.h>

#include <fmt/format.h>

#include <string>

namespace py = pybind11;

std::string greet(const std::string &name) {
  return fmt::format("Hello, {}!", name);
}

PYBIND11_MODULE(conan_hello, m) {
  m.def("greet", &greet, py::arg("name"));
}
