#!/usr/bin/python3
for i in range(0, 9):
    for j in range(0, 10):
        if i == 0:
            print("{}{}".format(i, j), end=", ")
        elif j < i:
            continue
        elif i == j:
            continue
        elif i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")
