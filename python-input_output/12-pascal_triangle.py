#!/usr/bin/python3
"""Defines a function."""


def pascal_triangle(n):
    """Returns lists of integers representing
    the Pascal's triangle of n."""
    if n <= 0:
        return []

    result = []
    last_list = []

    for i in range(1, n + 1):
        temp_list = []

        for j in range(0, i):
            if j == 0 or j == i - 1:
                temp_list.append(1)
            else:
                sum_two_nums = last_list[j] + last_list[j - 1]
                temp_list.append(sum_two_nums)

        result.append(temp_list)
        last_list = temp_list

    return result
