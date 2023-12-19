#!/usr/bin/python3
"""Creates a class Square"""


class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """ Initializes a new Square

        args:
            size(int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """setter/getter of size"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns:
            the area of the square
        """
        return self.__size**2

    def __eq__(self, other):
        """== comparison of two squares"""
        return self.area() == other.area()

    def __ne__(self, other):
        """!= comparison of two squares"""
        return self.area() != other.area()

    def __lt__(self, other):
        """< comparison of two squares"""
        return self.area() < other.area()

    def __le__(self, other):
        """<= comparison of two squares"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """> comparison of two squares"""
        return self.area() > other.area()

    def __ge__(self, other):
        """>= comparison of two squares"""
        return self.area() >= other.area()
