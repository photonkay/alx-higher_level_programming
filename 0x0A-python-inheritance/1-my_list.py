#!/usr/bin/python3

"""class that inherits another"""


class MyList(list):
    """This class inherits the list class"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
