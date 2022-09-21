#!/usr/bin/python3
'''Write a function that prints My name is <first name> <last name>

    first_name and last_name must be strings otherwise,
    raise a TypeError exception with the message first_name
    must be a string or last_name must be a string

    Returns the print
        '''


def say_my_name(first_name, last_name=""):
    """ a function that prints a string

        args:
            first_name: is the first string
            last_name: is the second string
        Return:
            My name is <first name> <last name>
    """
    if not first_name or type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print(f"My name is {first_name} {last_name:s}")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
