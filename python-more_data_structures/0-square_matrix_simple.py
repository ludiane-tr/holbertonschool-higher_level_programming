#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for num in matrix:
        new_num = [x**2 for x in num]
        new_matrix.append(new_num)
    return new_matrix
