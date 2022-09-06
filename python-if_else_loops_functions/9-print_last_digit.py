#!/usr/bin/python3
# Write a function that prints the last digit of a number


def print_last_digit(number):
    number = abs(number)
    print(f"{(number % 10)}", end='')
    return (number % 10)
