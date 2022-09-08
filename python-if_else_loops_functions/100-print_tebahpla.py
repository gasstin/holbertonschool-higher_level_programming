#!/usr/bin/python3
for n in range(122, 96, -1):
    if n % 2 == 0:
        m = 0
    else:
        m = 32
    print("{}".format(chr(n - m)), end='')
