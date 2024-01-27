#!/usr/bin/python3
def multiple_returns(sentence):
    """returns a tuple with the length of a string and its character"""
    len_char_tuple = (0, 'None')
    if sentence:
        len_char_tuple = (len(sentence), sentence[0])
    return len_char_tuple
