#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(my_list)
    sum_unique = 0
    for n in unique:
        sum_unique += n
    return sum_unique
