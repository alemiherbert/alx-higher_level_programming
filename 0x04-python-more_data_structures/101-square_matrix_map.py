#!/usr/bin/python3

def square_matric_map(matrix):
    new_matrix = matrix[:]
    return list(map(lambda x: list(map(lambda y: y * y, x)), new_matrix))
