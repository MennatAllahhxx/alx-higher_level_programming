#!/usr/bin/python3
def remove_char_at(str, n):
    retval = ""
    for i in range(len(str)):
        if i == n:
            continue
        retval += str[i]
    return retval
