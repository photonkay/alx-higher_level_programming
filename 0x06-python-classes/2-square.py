#!/usr/bin/python3

"""Continuing 1-square.py"""

class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initialise the dimensions of square

        Args:
            size (int): size of square
         """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
