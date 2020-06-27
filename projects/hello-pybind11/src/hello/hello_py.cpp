#include "hello.h"
#include <pybind11/pybind11.h>

namespace py = pybind11;
using namespace hello;

PYBIND11_MODULE(_hello, m) {
    m.doc() = "_hello"; // optional module docstring {
    m.def("hello", &hello::hello);
    m.def("return_two", &return_two);
}
