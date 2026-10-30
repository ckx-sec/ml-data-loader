#include <Python.h>

/* Placeholder for C-accelerated CSV parsing.
   Currently returns None; full implementation pending. */
static PyObject* accel_csv_parse(PyObject* self, PyObject* args) {
    Py_RETURN_NONE;
}

static PyMethodDef AccelMethods[] = {
    {"csv_parse", accel_csv_parse, METH_VARARGS, "C-accelerated CSV parsing."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef accelmodule = {
    PyModuleDef_HEAD_INIT,
    "_accel",
    "C extension module for accelerated CSV parsing.",
    -1,
    AccelMethods
};

PyMODINIT_FUNC PyInit__accel(void) {
    return PyModule_Create(&accelmodule);
}
