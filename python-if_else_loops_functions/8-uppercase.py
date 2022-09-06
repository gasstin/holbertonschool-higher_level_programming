#!/usr/bin/python3
# Write a function that prints a string in uppercase


def uppercase(str):
    for n in range(len(str)):
        if ord(str[n]) >= 97 and ord(str[n]) <= 122:
            c = chr(ord(str[n]) - 32)
        else:
            c = str[n]

        if n < (len(str) - 1):
            print("{}".format(c), end='')
        else:
            print("{}".format(c))
