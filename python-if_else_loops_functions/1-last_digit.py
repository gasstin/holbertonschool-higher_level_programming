#!/usr/bin/python3
# This program will assign a random signed number to the variable number
# each time it is executed. Complete the source code in order to print
# the last digit of the number stored in the variable number.
import random
number = random.randint(-10000, 10000)
str = f"Last digit of {number} is {number % 10}"
if (abs(number) % 10) > 5:
    print(f"{str} and is greater than 5")
elif (number % 10) == 0:
    print(f"{str} and is 0")
elif (abs(number) % 10) <= 5:
    print(f"{str} and is less than 6 and not 0")
