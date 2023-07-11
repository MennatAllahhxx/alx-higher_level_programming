#!/usr/bin/python3
"""
this is '0-read_file' module

this module contains 1 function: read_file(filename="")
"""


def read_file(filename=""):
    """
    a fun to read a file
    :param filename: the file to be read
    :return: prints the file content
    """
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")

