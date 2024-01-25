#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    is_divisible_list = [i % 2 == 0 for i in my_list]
    return is_divisible_list
