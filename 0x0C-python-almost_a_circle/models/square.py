#!/usr/bin/python3
"""Defines class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square object"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a square object
        Args:
            size (int): size of the square
            x (int): horizontal justification
            y (int): vertical justification
            id (int): id of the square object
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """setter/getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates a square object by assigning an argument to each
        attribute of the square object

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
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {'id': self.id,  'size': self.size, 'x': self.x, 'y': self.y}

    def __str__(self):
        """string representation of the square object"""
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.size))
