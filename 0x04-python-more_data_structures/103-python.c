#include <Python.h>

/**
 * print_python_list - Print information about a Python list
 * @p: PyObject pointer to a Python list
 */
void print_python_list(PyObject *p) {
    Py_ssize_t size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

/**
 * print_python_bytes - Print information about a Python bytes object
 * @p: PyObject pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p) {
    printf("[.] bytes object info\n");
    
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    
    Py_ssize_t size = PyBytes_Size(p);
    printf("  size: %ld\n", size);
    
    printf("  trying string: %.*s\n", (int) size, PyBytes_AsString(p));

    printf("  first 10 bytes: ");
    for (Py_ssize_t i = 0; i < size && i < 10; i++) {
        printf("%02x", (unsigned char) PyBytes_AsString(p)[i]);
        if (i < 9) {
            printf(" ");
        }
    }
    printf("\n");
}
