#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """adds 2 tuples"""
    tuple1 = tuple_a + (0, 0)
    tuple2 = tuple_b + (0, 0)

    combined_tuples = tuple1[0] + tuple2[0], tuple1[1] + tuple2[1]
    return combined_tuples
