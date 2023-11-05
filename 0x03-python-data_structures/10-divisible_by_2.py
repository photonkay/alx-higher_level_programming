#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    bool_list = [num % 2 == 0 for num in my_list]
    return bool_list
