#!/usr/bin/python3
"""
this is '1-my_list' module

this module 1-my_list contains 1 class: MyList(list)

the class MyList contains 1 method: print_sorted()
"""


class MyList(list):
    """
    a class to sort a list
    """

    def print_sorted(self):
        """
        a method to print a sorted list
        :return: prints sorted list
        """
        new_list = self.copy()
        new_list.sort()
        print(new_list)
