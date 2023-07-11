#!/usr/bin/python3
"""
this is '4-from_json_string' module

this module contains 1 function: from_json_string
"""
import json


def from_json_string(my_str):
    """
    a fun to return an obj from json
    :param my_str:  string to be converted
    :return: obj repr
    """
    return json.loads(my_str)
