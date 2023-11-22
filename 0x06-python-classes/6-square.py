#!/usr/bin/python3

"""Continuing 4-square.py"""


class Square:
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialise the dimensions of square

        Args:
            size (int): size of square
         """
        self.size = size
        self.position = position

    @property
    def position(self):
        """Returns the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the value of self.__position

        Args:
            value (tuple): this is the position of the #
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        """Returns the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of self.__size

        Args:
            value (int): this is the dimension
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
