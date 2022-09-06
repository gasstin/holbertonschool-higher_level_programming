#!/usr/bin/python3
# Write a program that imports the function def add(a, b):
# from the file add_0.py


def main():
    from add_0 import add
    a = 1
    b = 2
    c = add(a, b)
    print("{0} + {1} = {2}".format(a, b, c))
if __name__ == "__main__":
    main()
