#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject *hello_function(PyObject *self, PyObject *args) {
    PyObject* builtins = PyImport_ImportModule("builtins");
    PyObject* print = PyObject_GetAttrString(builtins, "print");
    PyObject* msg = PyUnicode_FromString("Hello, scikit-build-core CAPI fans!");
    PyObject* none = PyObject_CallOneArg(print, msg);

    Py_XDECREF(print);
    Py_XDECREF(builtins);
    Py_XDECREF(msg);
    Py_XDECREF(none);

    Py_RETURN_NONE;
}

static PyMethodDef skcdpure_methods[] = {
    {"hello", hello_function, METH_NOARGS, "Hello function"},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef skcdpure_module = {PyModuleDef_HEAD_INIT, "skcdpure",
                                             NULL, -1, skcdpure_methods};

PyMODINIT_FUNC PyInit_skcdpure(void) {
  return PyModule_Create(&skcdpure_module);
}
