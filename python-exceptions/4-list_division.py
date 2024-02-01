#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    if len(my_list_1) > len(my_list_2):
        list_len = len(my_list_1)
    else:
        list_len = len(my_list_2)

    res_list = []
    for i in range(list_len):
        try:
            res = my_list_1[i] / my_list_2[i]
        except TypeError:
            res = 0
            print("wrong type")
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            res_list.append(res)
    
    return res_list