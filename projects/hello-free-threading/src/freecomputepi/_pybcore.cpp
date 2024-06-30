#include <pybind11/pybind11.h>
#include <random>

namespace py = pybind11;

double pi(int n) {
    double sum = 0.0;

    std::random_device r;
    std::default_random_engine e1(r());
    std::uniform_real_distribution<double> uniform_dist(-1, 1);

    for (int i = 0; i < n; i++) {
        double x = uniform_dist(e1);
        double y = uniform_dist(e1);
        if (x * x + y * y <= 1.0) {
            sum += 1.0;
        }
    }
    return 4.0 * sum / n;
}

PYBIND11_MODULE(_pybcore, m, py::mod_gil_not_used()) {
    m.def("pi", &pi);
}
