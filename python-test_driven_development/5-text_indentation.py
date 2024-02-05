#!/usr/bin/python3
"""Defines text indentation"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: '.', '?', and ':'.

    Args:
        text (str): text to iterate and separate.
    
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1

#    for char in text:
#        if char == "":
#            pass
#        else:
#            print(char, end="")
#
#        if char in ".?:":
#            print("\n")        
