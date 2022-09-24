#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            counter = 1
            last = len(row)

            for num in row:
                # If the last one
                if i == last:
                    print('{:d}'.format(num), end="")
                else:
                    print('{:d}'.format(num), end=" ")
            print()
