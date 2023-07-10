#!/usr/bin/python3
"""
this is '0-lookup' module.

the 0-lookup module has one function :  lookup(obj)
"""


def lookup(obj):
    """
    a function to return list
    :param obj: object to be looked up
    :return: list of attributes and methods
    """
    return dir(obj)
