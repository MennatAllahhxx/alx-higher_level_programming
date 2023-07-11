#!/usr/bin/python3
"""
this is '101-add_attribute' module

this module contains 1 function: add_attribute
"""


def add_attribute(object, name, value):
    """
    a fun to add attribute if possible
    :param object: object to add attribute to
    :param name: name of the attribute
    :param value: value of the attribute
    :return: nth
    """
    if hasattr(object, "__dict__"):
        setattr(object, name, value)
    else:
        raise TypeError("can't add new attribute")
