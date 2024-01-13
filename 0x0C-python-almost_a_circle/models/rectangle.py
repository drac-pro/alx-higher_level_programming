#!/usr/bin/python3
"""Defines class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle object"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initiallizes a rectangle object
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): vertical justification when displaying rectangle
            y (int): horizontal justification when displaying rectangle
            id (int): rectangle id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Setter/getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Setter/getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Setter/getter of x"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Setter/getter of y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """computes the area of the rectangle object"""
        return (self.width * self.height)

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        [print() for _ in range(self.y)]
        [print(' '*self.x + '#'*self.width) for _ in range(self.height)]

    def update(self, *args, **kwargs):
        """updates a rectangle object by assigning an argument to each
        attribute of the rectangle object

        Args:
            args (tuple): variable arguments
            kwargs (dict): key/word variable arguments
        """
        if len(args) == 0:
            for name, value in kwargs.items():
                self.__setattr__(name, value)
        else:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}

    def __str__(self):
        """string representation of the rectangle object"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.x, self.y, self.width, self.height))
