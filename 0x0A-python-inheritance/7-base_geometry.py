#!/usr/bin/python3

"""based on 6-base_geometry.py"""


class BaseGeometry:
    """Base class"""
    def area(self):
        """Raises an exception since area was not called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
