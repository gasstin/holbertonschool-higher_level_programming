#!/usr/bin/python3
# Write a program that prints the ASCII alphabet,
# in lowercase, not followed by a new line.
for w in range(97, 123):
    if w == 101 or w == 113:
        continue
    else:
        print("{}".format(chr(w)), end='')
