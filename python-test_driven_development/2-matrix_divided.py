#!/usr/bin/python3
"""
This module defines a function that divide all elements of a matrix
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int/float): The divisor.

    Returns:
        list of lists of float: A new matrix with all elements divided by div.

    Raises:
        TypeError: If the matrix elements are not lists of int, floats.
                   If the rows of the matrix are not of the same size, or
                   if div is not an int, float.
        ZeroDivisionError: If the div is zero.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    for row in matrix:
        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(i / div, 2) for i in row] for row in matrix]
