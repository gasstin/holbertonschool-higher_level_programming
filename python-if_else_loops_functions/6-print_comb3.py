#!/usr/bin/python3
# Write a program that prints numbers from 0 to 99.
# Numbers must be separated by ,, followed by a space
# Numbers should be printed in ascending order, with two digits
for n in range(10):
    for m in range(n, 10):
        if n != m:
            if n == 8 and m == 9:
                print("{}{}".format(n, m))
            else:
                print("{}{}".format(n, m), end=', ')
