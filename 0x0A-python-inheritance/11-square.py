#!/usr/bin/python3
"""Defines a class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square object"""
    def __init__(self, size):
        """Initializes the Square object
        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """computes the area of the square"""
        return (self.__size**2)

    def __str__(self):
        """string representation of the class Square"""
        return "[Square] {}/{}".format(self.__size)
