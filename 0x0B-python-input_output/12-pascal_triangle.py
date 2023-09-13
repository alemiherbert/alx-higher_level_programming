#!/usr/bin/python3

"""
Pascals triangle
"""

def pascal_triangle(n):
    """ Pascals triangle """
    outer_list = []
    if n <= 0:
        return outer_list
    for i in range(1, n+1):
        inner_list = []

        head = 1
        for j in range(1, i+1):
            inner_list.append(head)

            head = head * (i - j) // j
        outer_list.append(inner_list)
    return outer_list
