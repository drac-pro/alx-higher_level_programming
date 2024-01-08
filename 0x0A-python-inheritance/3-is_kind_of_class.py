#!/usr/bin/python3
"""define is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """checks if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class
    Args:
        obj (object): an object instance
        a_class (type): a class
    Returns:
        bool: True or False
    """
    return True if isinstance(obj, a_class) else True
