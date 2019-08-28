#include "hello.h"
#include <pybind11/pybind11.h>

namespace py = pybind11;
using namespace hello;

void init_hello(py::module &m) {
    m.def("hello", &hello::hello);
    m.def("return_two", &return_two);
}
