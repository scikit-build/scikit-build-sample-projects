#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <random>


static PyObject * pi(PyObject *self, PyObject *arg) {
    int n = PyLong_AsLong(arg);
    if (n == -1 && PyErr_Occurred()) {
        return NULL;
    }
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

    return Py_BuildValue("d", 4.0 * sum / n);
}

extern "C" {

static PyMethodDef core_methods[] = {
    {"pi",  pi, METH_O, "Compute pi"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static int _core_exec(PyObject *m) {
    if (PyModule_AddFunctions(m, core_methods) < 0)
        return -1;
    return 0;
}

static PyModuleDef_Slot module_slots[] = {
    {Py_mod_exec, (void*) _core_exec},
    {Py_mod_multiple_interpreters, Py_MOD_PER_INTERPRETER_GIL_SUPPORTED},
    #ifdef Py_GIL_DISABLED
    {Py_mod_gil, Py_MOD_GIL_NOT_USED},
    #endif
    {0, NULL},
};

static struct PyModuleDef coremodule = {
    PyModuleDef_HEAD_INIT,
    "_core",
    NULL,
    0,
    core_methods,
    module_slots,
    NULL,
    NULL,
    NULL,
};


PyMODINIT_FUNC PyInit__core(void) {
    return PyModuleDef_Init(&coremodule);
}

};
