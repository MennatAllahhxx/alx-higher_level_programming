#!/usr/bin/python3
"""
this is '100-append_after' module

this module contains 1 function: append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    a fun to append a text to file after a line containing certain string
    :param filename:
    :param search_string: string to be searched for
    :param new_string: string to be appended
    :return: nth
    """
    with open(filename, 'r+', encoding="utf-8") as file:
        if not search_string or not new_string:
            return
        file_content = file.readlines()
        if not file_content:
            return
        index = 0
        found = False
        for line in file_content:
            if line.find(search_string) != -1:
                file_content.insert(index + 1, new_string)
                found = True
            index += 1
        if found:
            file.seek(0)
            file.write("".join(file_content))
