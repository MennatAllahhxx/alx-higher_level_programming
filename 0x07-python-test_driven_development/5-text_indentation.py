#!/usr/bin/python3
"""
this is '5-text_indentation' module.

the 5-text_indentation module has one function :  text_indentation(text)
"""


def text_indentation(text):
    """
    a fun to split text on multiple lines when it encounters '.','?',':'
    :param text: text to be split (str)
    :return: prints split text (str)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    splitters = [':', '.', '?']
    f = 0
    for i in text:
        if i in splitters:
            print(i)
            print()
            f = 1
        else:
            if f == 1 and i == " ":
                continue
            else:
                print(i, end="")
                f = 0
