#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    temp_a = tuple_a + (0, 0)
    temp_b = tuple_b + (0, 0)
    return (temp_a[0] + temp_b[0], temp_a[1] + temp_b[1])
