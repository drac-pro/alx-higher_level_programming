#!/usr/bin/python3
"""defines is_same_class function"""


def is_same_class(obj, a_class):
    """checks if an object is a dirrect instance of a class
    Args:
        obj (object): an object instance
        a_class (type): a class
    Returns:
        bool: True or False
    """
    return True if type(obj) is a_class else False
