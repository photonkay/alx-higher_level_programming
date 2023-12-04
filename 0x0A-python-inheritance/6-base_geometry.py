#!/usr/bin/python3

"""based on 5-base_geometry.py"""


class BaseGeometry:
    """Base class"""
    def area(self):
        """Raises an exception since area was not called"""
        raise Exception("area() is not implemented")
