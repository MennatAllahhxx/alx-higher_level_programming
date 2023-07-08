#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    a class to test max_integer
    """

    def test_module_docstring(self):
        """
        tests for module docstring
        :return: true if correct
        """
        self.assertTrue(len(__import__("6-max_integer").
                            __doc__) > 1)

    def test_function_docstring(self):
        """
        tests for function docstring
        :return: true if correct
        """
        self.assertTrue(len(__import__("6-max_integer").
                            max_integer.__doc__) > 1)

    def test_empty_list(self):
        """
        tests for empty list
        :return: true if correct
        """
        self.assertIsNone(max_integer([]))

    def test_regular_list1(self):
        """
        tests for regular list 1
        :return: true if correct
        """
        self.assertEquals(max_integer([1, 2, -2]), 2)

    def test_regular_list2(self):
        """
        tests for regular list 2
        :return: true if correct
        """
        self.assertEquals(max_integer([50, 2, -2]), 50)

    def test_regular_list3(self):
        """
        tests for regular list 3
        :return: true if correct
        """
        self.assertEquals(max_integer([-3, -70, -2]), -2)

    def test_regular_list4(self):
        """
        tests for regular list 4
        :return: true if correct
        """
        self.assertEquals(max_integer([2, 2, -2]), 2)

    def test_none(self):
        """
        tests for empty list
        :return: true if correct
        """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_string(self):
        """
        tests for string in a list
        :return: true if correct
        """
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, 'a'])

    def test_one_element(self):
        """
        tests for only one number in the list
        :return: true if correct
        """
        self.assertEqual([1], 1)


if __name__ == "__main__":
    unittest.main()
