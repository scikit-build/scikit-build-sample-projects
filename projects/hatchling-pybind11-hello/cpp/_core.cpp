#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(_core, m) {
    m.def("hello", [](){
        py::print("Hello, scikit-build!");
    });
}
