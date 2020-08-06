#include "hello.hpp"
#include <pybind11/pybind11.h>


PYBIND11_MODULE(_hello, m) {
    m.doc() = "Example module";
    m.def("hello", &hello::hello, "Prints \"Hello, World!\"");
    m.def("return_two", &hello::return_two, "Returns 2");
}
