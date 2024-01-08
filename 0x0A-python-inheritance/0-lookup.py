#!/usr/bin/python3
"""defines a lookup function"""


def lookup(obj):
    """returns a list of available attributes and methods of an object
    Args:
        obj (object): an object
    Returns:
        list: list of attributes and methods of the object
    """
    if isinstance(obj, object):
        return dir(obj)
