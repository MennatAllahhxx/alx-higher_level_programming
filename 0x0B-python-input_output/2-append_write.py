#!/usr/bin/python3
"""
this is '2-append_write' module

this module contains 1 function: append_write
"""


def append_write(filename="", text=""):
    """
    a fun to append to a file
    :param filename: file to be appended to
    :param text: text to be appended
    :return: number of chars appended
    """
    with open(filename, 'a', encoding="utf-8") as file:
        num = file.write(text)
        return num
