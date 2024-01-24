#!/usr/bin/python3
import sys
num_args = sys.argv
args_len = len(num_args) - 1

print("{}".format(args_len), end=" ")
if args_len == 0:
    print("arguments:")
elif args_len == 1:
    print("argument:")
else:
    print("arguments:")

for i in range(args_len):
    print("{}: {}".format(i + 1, num_args[i + 1]))

