#!/usr/bin/python3
def main():
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    c = add(a, b)
    d = sub(a, b)
    e = mul(a, b)
    f = div(a, b)
    print("{0} + {1} = {2}".format(a, b, c))
    print("{0} - {1} = {2}".format(a, b, d))
    print("{0} * {1} = {2}".format(a, b, e))
    print("{0} / {1} = {2}".format(a, b, f))


if __name__ == "__main__":
    main()
