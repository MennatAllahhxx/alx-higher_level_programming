#!/usr/bin/python3
"""
this is '2-matrix_divided' module.

the 2-matrix_divided module has one function :  matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """
    a function to divide a matrix by a certain number
    :param matrix: matrix to be divided (list)
    :param div: divisor (int or float)
    :return: divided_matrix (list)
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if not all(isinstance(i, list) for i in matrix) or not\
            all(isinstance(j, (int, float)) for i in matrix for j in i):
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    size = len(matrix[0])
    for i in matrix:
        if size != len(i):
            raise TypeError("Each row of the matrix must have \
the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    divided_matrix = [[round(j/div, 2) for j in i] for i in matrix]
    return divided_matrix
