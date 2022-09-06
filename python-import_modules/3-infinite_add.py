#!/usr/bin/python3
def arguments_sum(arguments):
    sum = 0
    for n in range(1, len(arguments)):
        sum += int(arguments[n])
    print("{}".format(sum))


if __name__ == "__main__":
    import sys
    arguments_sum(sys.argv)
