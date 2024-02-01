#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string == "None":
        return 0
    else:
        def roman_converter(r):
            roman_numbers = {
                    'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000}
            if r not in roman_numbers:
                return -1
            else:
                return roman_numbers[r]

        result = 0
        i = 0
        while i < len(roman_string):
            curr_num = roman_converter(roman_string[i])
            
            if i + 1 < len(roman_string):
                next_num = roman_converter(roman_string[i + 1])
                if curr_num >= next_num:
                    result += curr_num
                    i += 1
                else:
                    result += next_num - curr_num
                    i += 2
            else:
                result += curr_num
                i += 1

        return result
