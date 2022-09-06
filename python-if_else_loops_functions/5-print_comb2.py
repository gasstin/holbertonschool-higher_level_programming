#!/usr/bin/python3
# Write a program that prints numbers from 0 to 99.
# Numbers must be separated by ,, followed by a space
# Numbers should be printed in ascending order, with two digits
for n in range(0, 100):
    if n < 99:
        print("{:02}".format(n), end="")
    else:
        print(n)
