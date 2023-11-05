#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            print("{}".format(matrix[i][j]), end=" ")
        print()
