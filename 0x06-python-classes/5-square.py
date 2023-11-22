#!/usr/bin/python3

"""Continuing 4-square.py"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initialise the dimensions of square

        Args:
            size (int): size of square
         """
        self.size = size

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
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
