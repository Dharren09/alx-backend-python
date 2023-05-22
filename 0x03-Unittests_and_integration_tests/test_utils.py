#!/usr/bin/env python3
"""uses a function, plays with the python console and tests the method
the body of the test method should not be longer than 2 lines"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Dict, Tuple, Union
access_nested_map = __import__("utils").access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """using a decorator to test the function for the following inputs"""
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Tuple,
                               expected: Union[int, str]):
        """asserting the function that returns the expected result or
        AssertError is otherwise"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',) KeyError("Key not found: 'a'")),
        ({'a': 1}, ('a', 'b'), KeyError("Key not found: 'b'")),
    ])
    def test_access_nested_map_exception(self, nested_map: Dict, path: Tuple,
                                         expected: Union[int, str]):
        """Tests raise of keyError exception"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), str(expected_exception))


if __name__ == "__main__":
    unittest.main()
