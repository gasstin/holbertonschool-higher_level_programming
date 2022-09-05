#!/usr/bin/python3
# This program will assign a random signed number to the variable number
# each time it is executed. Complete the source code in order to print
# the last digit of the number stored in the variable number.
import random
number = random.randint(-10000, 10000)
str = f"Last digit of {number}"
if number > 0:
    if (number % 10) > 5:
        print(f"{str} is {number % 10} and is greater than 5")
    elif (number % 10) == 0:
        print(f"{str} is {number % 10} and is 0")
else:
    number = number * -1
    if (number % 10):
        print(f"{str} is -{number % 10} and is less than 6 and not 0")
    else:
        print(f"{str} is {number % 10} and is 0")
