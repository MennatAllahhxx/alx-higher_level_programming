#!/usr/bin/python3
"""
this is '12-pascal_triangle' module

this module contains 1 function: pascal_triangle
"""


def pascal_triangle(n):
    """
    a fun to return list of list
    :param n: number of lists
    :return: list of lists of integers
    """
    if n <= 0:
        return []

    my_list = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(my_list[i - 1][j - 1] + my_list[i - 1][j])
        row.append(1)
        my_list.append(row)

    return my_list
