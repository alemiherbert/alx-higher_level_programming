#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    temp_a = temp_b = ()
    if len(tuple_a) == 0:
        temp_a = (0, 0)
    if len(tuple_b) == 0:
        temp_b = (0, 0)

    if len(tuple_a) == 1:
        temp_a = (tuple_a[0], 0)
    if len(tuple_b) == 1:
        temp_b = (tuple_b[0], 0)

    if len(tuple_a) >= 2:
        temp_a = (tuple_a[0], tuple_a[1])
    if len(tuple_b) >= 2:
        temp_b = (tuple_b[0], tuple_b[1])
    return (temp_a[0] + temp_b[0], temp_a[1] + temp_b[1])
