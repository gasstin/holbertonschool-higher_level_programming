#!/usr/bin/python3
def main():
    import hidden_4
    for w in dir(hidden_4):
        if w[0] != '_':
            print("{}".format(w))


if __name__ == "__main__":
    main()
