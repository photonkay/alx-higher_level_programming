#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        max = my_list[0]
        for elem in my_list:
            if elem > max:
                max = elem
        return max
    else:
        return None
