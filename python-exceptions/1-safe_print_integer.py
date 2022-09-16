#!/usr/bin/python3
# Write a function that prints an integer with "{:d}".format().


def safe_print_integer(value):
    try:
        print(f"{value:d}")
        return (True)
    except Exception:
        return (False)
