#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""
    def test_module_docstring(self):
        """tests  docstring"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """tests function docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_empty_list(self):
        """tests for empty list"""
        self.assertIsNone(max_integer([]), None)

    def test_no_args(self):
        """tests for no arguments"""
        self.assertIsNone(max_integer(), None)

    def test_one_arg(self):
        """tests for 1 argument"""
        self.assertEqual(max_integer([1]), 1)

    def test_int(self):
        """test for integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 1, 3, 2]), 4)
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1, 4, 3, 2, 4]), 4)

    def test_float(self):
        """tests for floats"""
        self.assertEqual(max_integer([1.10, 1.01, 1.11, 1.001]), 1.11)

    def test_string(self):
        """tests for strings"""
        self.assertEqual(max_integer(["a", "b", "c", "d"]), "d")

    def test_dict(self):
        """tests for dict"""
        with self.assertRaises(KeyError):
            max_integer({1: "a", 2: "b"})

    def test_tuple(self):
        """tests for tuple"""
        self.assertEqual(max_integer((1, 2, 3)), 3)

    def test_none(self):
        """Tests for None"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_mixed(self):
        """Tests mixed types in list"""
        lst = [1, "yes", 3.5]
        with self.assertRaises(TypeError):
            max_integer(lst)

    def test_inf(self):
        """tests for infinity"""
        self.assertEqual(max_integer([float('inf'), 1]), float('inf'))

    def test_neg_inf(self):
        """tests for negative infinity"""
        self.assertEqual(max_integer([float('-inf'), 1]), 1)

if __name__ == "__main__":
    unittest.main()