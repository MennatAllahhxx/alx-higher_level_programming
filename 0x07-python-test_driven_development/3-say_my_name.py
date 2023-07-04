#!/usr/bin/python3
"""
this is '3-say_my_name' module.

the 3-say_my_name module has one function :  \
        say_my_name(first_name, last_name="")
"""


def say_my_name(first_name, last_name=""):
    """
    a function to print my name
    :param first_name: my first name (str)
    :param last_name: my last name (str)
    :return: prints "My name is <first name> <last name>"
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
