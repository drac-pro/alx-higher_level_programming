#!/usr/bin/python3
"""Defines add_attribute function"""


def add_attribute(obj, name, value):
    """sets an object attribute if posible
    Args:
        obj (object): an object instance
        name (str): name of attribute
        value (any type): attribute value
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
