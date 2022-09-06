#!/usr/bin/python3
# comentario


def uppercase(str):
    for n in range(0, len(str)):
        if ord(str[n]) >= 97 and ord(str[n]) <= 122:
            c = chr(ord(str[n]) - 32)
        else:
            c = str[n]

        print("{}".format(c), end='')
    print('')
