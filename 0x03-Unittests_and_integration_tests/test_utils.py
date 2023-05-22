#!/usr/bin/env python3
"""uses a function, plays with the python console and tests the method
the body of the test method should not be longer than 2 lines"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Dict, Tuple, Union
access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json


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
        ({}, ('a',)),
        ({'a': 1}, ('a', 'b')),
    ])
    def test_access_nested_map_exception(self, nested_map: Dict, path: Tuple):
        """Tests raise of keyError exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """class tests the utils.get_json"""
    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url: str, expected: Dict):
        """tests get_json, creates a mock object for the requests.get
        function"""
        mock_get = Mock()
        """configures the mock object to return the expected result"""
        mock_get.json.return_value = expected

        """patch the requestd.get function with mock object the assigns it
        to the mock_request variable"""
        with patch("requests.get", return_value=mock_get) as mock_request:
            result = get_json(test_url)
            self.assertEqual(result, expected)
            mock_request.assert_called_once()


if __name__ == "__main__":
    unittest.main()
