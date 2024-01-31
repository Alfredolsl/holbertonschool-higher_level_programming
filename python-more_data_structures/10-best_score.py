#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest
    integer value"""
    if a_dictionary:
        score = 0
        leader = ""
        for key in a_dictionary:
            if a_dictionary[key] > score:
                score = a_dictionary[key]
                leader = key
        return leader
