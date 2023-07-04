#!/usr/bin/python3
"""
New class
"""


class Rectangle:
    """
    a class to define a rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initialize parameters of a rectangle
        :param width: width of rect (int)
        :param height: height of rect (int)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        """
        a method to change private width attribute
        :param self: Rectangle (class)
        :param width: width (int)
        :return: changed width
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        """
        a method to change private height attribute
        :param self: Rectangle (class)
        :param height: height (int)
        :return: changed height
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        """
        a method to calculate area of a rectangle
        :return: area (int)
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        a method to calculate perimeter of a rectangle
        :return: perimeter (int)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """
        a method to represent rectangle using str
        :return: s in # (str)
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            s = ""
            for i in range(self.__height):
                s += self.__width * str(self.print_symbol)
                if not (i == (self.__height - 1)):
                    s += '\n'
            return s

    def __repr__(self):
        """
        a method to repr rectangle to be used by eval
        :return: Rectangle(width, height) (str)
        """
        return "Rectangle(" + str(self.__width) + ", " +\
            str(self.__height) + ")"

    def __del__(self):
        """
        a method to delete rectangle
        :return: nth
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        a method to check for bigger rectangle
        :param rect_1: 1st rectangle (Rectangle)
        :param rect_2: 2nd rectangle (Rectangle)
        :return: biggest rectangle (Rectangle)
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2
