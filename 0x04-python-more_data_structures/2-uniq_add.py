#!/usr/bin/python3
def uniq_add(my_list=[]):
    uni = set(my_list)
    res = 0
    for i in uni:
        res = i + res
    return res
