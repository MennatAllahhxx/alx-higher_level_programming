#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        i = -1 * number
    else:
        i = number
    while i > 9:
        i %= 10
    print("{}".format(i), end="")
    return i
