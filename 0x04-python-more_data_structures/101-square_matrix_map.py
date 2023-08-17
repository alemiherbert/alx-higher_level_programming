#!/usr/bin/python3

def square_matrix_map(matrix):
    new = matrix[:]
    new = list(map(lambda x: list(map(lambda y: y * y, x)), new))
    return new
