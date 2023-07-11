#!/usr/bin/python3
"""
this is '1-write_file' module

this module contains 1 function: write_file
"""


def write_file(filename="", text=""):
    """
    a fun to write to a file
    :param filename: file to be written to
    :param text: text to be written
    :return: number of chars written
    """
    with open(filename, 'w', encoding="utf-8") as file:
        num = file.write(text)
        return num
