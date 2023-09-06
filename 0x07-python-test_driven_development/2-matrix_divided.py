#!/usr/bin/python3

"""
Defines matrix division functions
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Args:
        matrix (list): a list of lists of ints or floats
        div (int/float): the divisor

    Raises:
        TypeError: if matrix is not a list of integers or floats
        TypeError: if each row of the matrix is not the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div is a zero
    """

    if not (isinstance(matrix, list) and
            all(isinstance(row, list) and
            all(isinstance(i, (int, float)) for i in row)
            for row in matrix)) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not type(div) is int and not type(div) is float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]