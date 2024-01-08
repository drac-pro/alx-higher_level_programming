#!/usr/bin/python3
""""""


def is_same_class(obj, a_class):
    """checks if an object is a dirrect instance of a class
    Args:
        obj (object): an object instance
        a_class (type): a class
    Returns:
        bool: True or False
    """
    if isinstance(obj, object) and isinstance(a_class, type):
        return True if type(obj) == a_class else False
