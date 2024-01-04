#!/usr/bin/python3
"""creates a Rectangle class"""


class Rectangle:
    """Defines a rectangle object"""
    def __init__(self, width=0, height=0):
        """initializes a rectangle object
        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
        """
        self.width = width
        self.height = height

    def __del__(self):
        """method called when an instance of rectangle is deleted"""
        print("Bye rectangle...")

    @property
    def width(self):
        """setter/getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """setter/getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Compute the area of the rectangle object"""
        return (self.__width * self.height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        row = '#' * self.__width
        return '\n'.join([row] * self.__height)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
