#!//usr/bin/python3
"""uses a function, plays with the python console and tests the method
the body of the test method should not be longer than 2 lines"""

import unittest
from utils import access_nest_map
from parameterized import parameterized
from unittest.mock import patch, Mock
from typing import Dict, Tuple, Union


class TestAccessNestedMap(unittest.TestCase):
    """using a decorator to test the function for the following inputs"""
    @parameterized.expand([
        ({"a": 1}, ("a",)),
        ({"a": {"b": 2}}, ("a",)),
        ({"a": {"b": 2}}, ("a", "b")),
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Tuple,
                               expected: Union[int, str]):
        self.assertEqual(access_nested_map(nested_map, path), nested_map[path])


if __name__ == "__main__":
    unittest.main()
