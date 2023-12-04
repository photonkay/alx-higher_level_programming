#!/usr/bin/python3

"""class that inherits another"""


class MyList(list):
    """This class inherits the list class"""
    def __init__(self):
         """initializes the object"""
         super().__init__()

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
