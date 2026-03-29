#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test list with one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_multiple_elements(self):
        """Test list with multiple elements"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_list(self):
        """Test unsorted list"""
        self.assertEqual(max_integer([3, 1, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test list with positive and negative numbers"""
        self.assertEqual(max_integer([-10, 5, 3, -1]), 5)

    def test_duplicate_max(self):
        """Test list with duplicate max values"""
        self.assertEqual(max_integer([1, 3, 3, 2]), 3)

    def test_all_same(self):
        """Test list where all elements are the same"""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_max_at_beginning(self):
        """Test max value at the beginning"""
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_max_at_end(self):
        """Test max value at the end"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)


if __name__ == "__main__":
    unittest.main()
