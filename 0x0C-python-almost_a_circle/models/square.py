#!/usr/bin/python3

"""Module of square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates the square class

        Args:
            size (int): width and height of square
            x (int): x coordinate
            y (int): y coordinate
            id (int): square id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation peculiar to Square instance"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Returns the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes of the Square instance.

        Args:
            *args: list of arguments
            *kwargs: keyworded arguments
        """
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dict representation of the Square"""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.width,
            'y': self.y
        }
