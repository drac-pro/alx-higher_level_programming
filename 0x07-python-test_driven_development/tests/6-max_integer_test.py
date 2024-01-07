#!/usr/bin/python3
"""ttest for max_integer()"""
import unittest
max_integer = __import__('6-max_integer').max_integer



class TestMaxInteger(unittest.TestCase):
    """unittest for max_integer"""
    def test_ordered_list_numbers(self):
        """test list"""
        lst = [1, 4, 5, 9]
        self.assertEqual(max_integer(lst), 9)

    def test_unordered_list_numbers(self):
        """test unordered list numbers"""
        lst = [4, -2, 1, 9, -3]
        self.assertEqual(max_integer(lst), 9)

    def test_empty_list(self):
        """test empty list"""
        lst = []
        self.assertIsNone(max_integer(lst))

    def test_no_input(self):
        """test no input"""
        self.assertIsNone(max_integer())

    def test_string(self):
        """test string"""
        lst = "hello"
        self.assertEqual(max_integer(lst), 'o')

    def test_list_of_strings(self):
        """test list of strings"""
        lst = ["can", "care", "hello", "me"]
        self.assertEqual(max_integer(lst), "me")

    def test_mixed_strings_and_numbers(self):
        """test mixed strings and numbers"""
        lst = [2, 4, "hello", 3]
        self.assertRaises(TypeError, max_integer, lst)

    def test_None(self):
        """test None"""
        self.assertRaises(TypeError, max_integer, None)
