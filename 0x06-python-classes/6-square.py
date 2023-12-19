#!/usr/bin/python3
"""Creates a class Square"""


class Square:
    """Represent a square"""
    def __init__(self, size=0, position=(0, 0)):
        """ Initializes a new Square

        args:
            size(int): size of the square
            position(tuple): position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """setter/getter of size"""
        return self.__size

    @property
    def position(self):
        """setter/getter of position"""
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if not all(type(x) is int for x in value) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns:
            the area of the square
        """
        return self.__size**2

    def my_print(self):
        """prints the square with the character #"""
        if self.__size == 0:
            print('')
            return
        [print('') for i in range(self.__position[1])]
        for i in range(self.__size):
            print(" "*self.__position[0], end='')
            print('#'*self.__size, end='')
            print('')
