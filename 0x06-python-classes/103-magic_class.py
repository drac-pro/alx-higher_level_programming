#!/usr/bin/python3
"""Creates a class MagicClass"""


import math


class MagicClass:
    """Template for a MagicClass"""
    def __init__(self, radius=0):
        """Initializes a circle

        Args:
            radius(int/float): radius of the circle
        """
        if type(radius) is not int or if type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculates area of circle"""
        return (self.__radius**2 * math.pi)

    def circumference:
        """Calculates circumference of circle"""
        return (2 * math.pi * self.__radius)
