#!/usr/bin/python3
"""creates a Rectangle class"""


class Rectangle:
    """Defines a rectangle object"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes a rectangle object
        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """method called when an instance of rectangle is deleted"""
        Rectangle.number_of_instances -= 1
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
        row = str(self.print_symbol) * self.__width
        return '\n'.join([row] * self.__height)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compares which rectangle is bigger
        Args:
            rect_1(Rectangle): a Rectangle instance
            rect_2(Rectangle): a Rectangle instance
        Returns:
            Rectangle: the biggest rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Creates a squre Rectangle instance
        Args:
            size(int): size of the square
        Returns:
            Rectangle: new square Rectangle
        """
        return cls(size, size)
