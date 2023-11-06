#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for cols in rows:
            print("{:d}".format(cols), end=" " if cols != rows[-1] else "")
        print()
