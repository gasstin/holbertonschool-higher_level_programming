#!/usr/bin/python3
# Write a function that prints the numbers
# from 1 to 100 separated by a space.
# For multiples of three print Fizz instead of the number
# and for multiples of five print Buzz.


def fizzbuzz():
    for n in range(1, 101):
        if (n % 3 == 0):
            print("Fizz", end=' ')
        elif (n % 5 == 0):
            print("Buzz", end=' ')
        elif (n % 5 == 0) and (n % 3 == 0):
            print("FizzBuzz", end=' ')
        elif n == 100:
            print("Buzz")
        else:
            print(f"{n}", end=' ')
