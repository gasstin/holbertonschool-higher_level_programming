#!/usr/bin/python3
# Create a function that converts a Roman numeral to an integer.


def roman_to_int(roman_string):
    result = 0
    if roman_string and isinstance(roman_string, str):
        daux = dict(zip(['I', 'V', 'X', 'L', 'C', 'D', 'M'],
                        [1, 5, 10, 50, 100, 500, 1000]))
        for k in range(len(roman_string)):
            result += daux[roman_string[k]]

            if len(roman_string) == 2 and k:
                if daux[roman_string[k - 1]] < daux[roman_string[k]]:
                    result -= 2 * daux.get(roman_string[k - 1])
            elif len(roman_string) > 2 and k + 1 < len(roman_string):
                if k - 1 >= 0 and daux[roman_string[k - 1]] < daux[roman_string[k]]:
                    if daux[roman_string[k + 1]] != daux[roman_string[k]]:
                        result -= 2 * daux[roman_string[k - 1]]
    return (result)
