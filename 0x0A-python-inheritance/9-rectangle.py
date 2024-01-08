#!/usr/bin/python3
"""Defines a class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a Rectangle object"""
    def __init__(self, width, height):
        """Initializes the Rectangle object
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """computes the area of a rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """custom str() method"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
