#!/usr/bin/python3
"""
this is '0-add_integer' module.

the 0-add_integer module has one function : add_integer(a, b)
"""


def add_integer(a, b=98):
    """
    a function to add two integers
    :param a: 1st integer (int or float)
    :param b: 2nd integer (int or float)
    :return: addition of a and b (int)
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a) + (b)
