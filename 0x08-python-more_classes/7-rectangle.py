#!/usr/bin/python3

"""Defines a rectangle (based on 0-rectangle.py)"""


class Rectangle:
    """Defines a rectangle's width

    Args:
        number_of_instances (int): number of objects created
        print_symbol (any): used as symbol for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Set the width and height of the rectangle

        Args:
            width (int): rectangle's width
            height (int): rectangle's height
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle

        Args:
            value (int): value of the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle

        Args:
            value (int): value of the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            for j in range(self.__width):
                rect.append(str(self.print_symbol))
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints bye bye when instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
