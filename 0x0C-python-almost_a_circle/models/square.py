#!/usr/bin/python3
"""
this is 'square' module

this module contains 1 class: Square

this class contains 3 methods: area, display, update

Rectangle class is imported
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    a new class for squares
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initialize object
        :param size: size of sq
        :param x: x-axis position
        :param y: y-axis position
        :param id: id of the class
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        """
        a method to change private size attribute
        :param size: given size
        :return: changed size
        """
        self.width = size
        self.height = size

    def __str__(self):
        """
        a method to repr string
        :return: representation
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
