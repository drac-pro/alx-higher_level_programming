#!/usr/bin/python3
"""Define inherits_from function"""


def inherits_from(obj, a_class):
    """checks if the object is an instance of a class that inherited (directly
    or indirectly) from the specified class
    Args:
        obj (object): an object instance
        a_class (type): a class
    Returns:
        bool: True or False
    """
    return True if issubclass(type(obj), a_class) and type(obj) is not \
        a_class else False
