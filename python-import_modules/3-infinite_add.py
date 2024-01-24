#!/usr/bin/python3

if __name__ == "__main__":
    """prints the result of the addition of all args"""
    import sys
    argc = len(sys.argv) - 1

    num_sum = 0

    for i in range(argc):
        num_sum += int(sys.argv[i + 1])

    print("{}".format(num_sum))
