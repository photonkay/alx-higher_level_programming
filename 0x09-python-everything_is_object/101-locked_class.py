#!/usr/bin/python3

"""A class with no class attributes"""


class LockedClass:
    """This class has no attribures except
       if the new instance is called first_name
    """
    __slots__ = ['first_name']
