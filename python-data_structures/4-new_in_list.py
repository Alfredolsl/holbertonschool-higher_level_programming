#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """replaces an element in a list at a specific
    pos without modifying the original list"""
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.copy()

    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
