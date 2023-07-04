#!/usr/bin/python3
"""
this is '4-print_square' module.

the 4-print_square module has one function :  print_square(size)
"""


def print_square(size):
    """
    a function to print a square of certain size
    :param size: side length of square (int)
    :return: prints square in shape of "#"
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
