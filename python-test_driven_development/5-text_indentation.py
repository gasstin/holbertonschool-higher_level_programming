#!/usr/bin/python3
''' Write a function that prints a text with 2 new lines after
    each of these characters: ., ? and :

    ext must be a string, otherwise raise a TypeError exception with the message
    text must be a string
    There should be no space at the beginning or at the end of each printed line
'''


def text_indentation(text):
    """ Write a function that prints a text

        args:
            text: is the text to print
        Return:
            print the separeted text
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    for i in range(len(text)):
        if text[i - 1] in [".", "?", ":"]:
            continue
        else:
            print(f"{text[i]}", end='')
        if text[i] in [".", "?", ":"]:
            print("\n")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
