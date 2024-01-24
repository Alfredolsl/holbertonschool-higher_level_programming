#!/usr/bin/python3
import sys
num_args = sys.argv
args_len = len(num_args) - 1

print("{} arguments".format(args_len), end="")
if args_len > 0:
    print(":")
else:
    print(".")

for i in range(args_len):
    print("{}: {}".format(i + 1, num_args[i + 1]))

