#!/usr/bin/python3
"""
this is 'rectangle' module

this module contains 1 class: Rectangle

this class contains 4 methods: area, display, update, to_dictionary

Base class is imported
"""
from models.base import Base


class Rectangle(Base):
    """
    a new class for rectangles
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialize object
        :param width: width of rect
        :param height: height or rect
        :param x: x-axis position
        :param y: y-axis position
        :param id: id of the class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        getter for width
        :return: nth
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        a method to change private width attribute
        :param width: given width
        :return: changed width
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        getter for height
        :return: nth
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        a method to change private height attribute
        :param height: given height
        :return: changed height
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
            getter for x
            :return: nth
            """
        return self.__x

    @x.setter
    def x(self, x):
        """
        a method to change private x attribute
        :param x: given x
        :return: changed x
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
            getter for y
            :return: nth
            """
        return self.__y

    @y.setter
    def y(self, y):
        """
        a method to change private y attribute
        :param y: given y
        :return: changed y
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        a method to calculate the area
        :return: area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        to display the rectangle
        :return: prints the rectangle
        """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        a method to repr string
        :return: representation
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        method to assign args to attrs
        :param args: arguments
        :param kwargs: keyword-arguments
        :return: attributes
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
        if len(args) <= 0:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        method to return dict of class
        :return: dictionary
        """
        dictionary = {"x": self.x,
                      "y": self.y,
                      "id": self.id,
                      "height": self.height,
                      "width": self.width}
        return dictionary
