#!/usr/bin/python3
# Write a function that prints an integer with "{:d}".format().
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return (False)
    return (True)
