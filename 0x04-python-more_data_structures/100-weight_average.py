#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0

    average = 0
    sum_of_weights = 0
    number_of_weights = 0
    for i in range(len(my_list)):
        sum_of_weights += my_list[i][0] * my_list[i][1]
        number_of_weights += my_list[i][1]
    return sum_of_weights / number_of_weights
