#!/usr/bin/python3


"""
1-matrix_divided.py - This module contains a function that divides
the elements of a matrix by a number
"""


def matrix_divided(matrix, div):
    """This function divides every element of matrix by div"""
    # Check whether the matrix is valid
    new_matrix = []
    for element in matrix:
        if not type(element) is list:
            raise TypeError("Matrix must be a matrix (list of lists) of integers/floats")
        for number in element:
            if not type(number) is int and not type(number) is float:
                raise TypeError("Matrix must be a matrix (list of lists) of integers/floats")
            number = number / div
        new_matrix.append(element)
    return new_matrix    


