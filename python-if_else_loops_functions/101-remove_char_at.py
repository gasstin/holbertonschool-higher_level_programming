#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        str_cp = ''
        for i in range(len(str)):
            if i == n:
                continue
            str_cp += str[i]
    else:
        str_cp = str
    return (str_cp)
