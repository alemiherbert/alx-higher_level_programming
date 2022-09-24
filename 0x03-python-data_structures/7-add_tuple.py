#!/usr/bin/python3
def for_more2(li):
    if len(li) > 2:
        li = li[:2]
    return li


def for_less2(li):
    if len(li) == 0:
        li.append(0)
    if len(li) == 1:
        li.append(0)
        li.append(0)
    return li


def add_tuple(tuple_a=(), tuple_b=()):
    nlist = []
    a = for_more2(for_less2(list(tuple_a)))
    b = list(tuple_b)
    for_more2(b)
    for_less2(b)
    for first, second in zip(a, b):
        num = first + second
        nlist.append(num)
    return tuple(nlist)
