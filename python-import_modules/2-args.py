#!/usr/bin/python3
def arguments_count(arguments):
    if (len(arguments) - 1) == 0:
        print("0 arguments.")
    elif (len(arguments) - 1) == 1:
        print("1 argument:")
        print("1: {0}".format(arguments[1]))
    else:
        print("{0} arguments:".format((len(arguments) - 1)))
        for n in range(1, len(arguments)):
            print("{0}: {1}".format(n, arguments[n]))


if __name__ == "__main__":
    import sys
    arguments_count(sys.argv)
