#!/usr/bin/python3
"""
this is '8-class_to_json' module

this module contains 1 function: class_to_json
"""


def class_to_json(obj):
    """
    a fun to return dict description
    :param obj: object
    :return: dict description
    """
    return obj.__dict__
