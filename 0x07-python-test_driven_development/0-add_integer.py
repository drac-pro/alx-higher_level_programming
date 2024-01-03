#!/usr/bin/python3
"""Creates a module 0-add_integer"""


def add_integer(a, b=98):
    """adds two integers to gether
    Args:
        a (int/float): the first number
        b (int/float): the second number
    Returns:
        int: the result of addition
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
