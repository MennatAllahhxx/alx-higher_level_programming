#!/usr/bin/python3
"""
this is '3-to_json_string' module

this module contains 1 function: to_json_string
"""
import json


def to_json_string(my_obj):
    """
    a fun to return json repr of an obj
    :param my_obj:  object to be json-repr
    :return: json representation
    """
    return json.dumps(my_obj)
