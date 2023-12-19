#!/usr/bin/python3
"""Creates a class Square"""


class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """ Initializes a new Square

        args:
            size(int): size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
