#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """An empty class BaseGeometry"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates if value is int and greater or equal to 0
        Args:
            name (str): field name
            value (int): value
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
