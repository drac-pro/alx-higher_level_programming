#!/usr/bin/python3
"""4-print_square module"""


def print_square(size):
    """ print a square with the character #
    Args:
        size: size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
