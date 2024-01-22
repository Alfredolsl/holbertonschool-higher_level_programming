#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print("{} ".format(number), end="")
if number > 0:
    print(f"is positive")
elif number == 0:
    print (f"is zero")
else:
    print(f"is negative")
