/** This file defines the module, the implementation can be
 * splitted in different cpp files
 */
#include <pybind11/pybind11.h>
namespace py = pybind11;

void init_hello(py::module &);
// void init_a_new_submodule_in_other_cpp_file(py::module &)

PYBIND11_MODULE(_hello, m) {
    m.doc() = "_hello"; // optional module docstring
    init_hello(m);
}
