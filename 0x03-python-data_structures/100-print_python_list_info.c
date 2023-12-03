#include <Python.h>

/**
 * print_python_list_info - print info about a python list
 *
 * @p: pointer to python list object
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int i, size, allocated;
	PyObject *item;

	if (!PyList_Check(p))
		return;
	size = Py_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
