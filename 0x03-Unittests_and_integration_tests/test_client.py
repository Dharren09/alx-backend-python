#!/usr/bin/env python3

import unittest
from unittest.mock import patch, Mock, PropertyMock, call
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from requests import HTTPError
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """Class to test GithubOrgClient"""

    @parameterized.expand([
        ('google', {'name': 'google'}),
        ('abc', {'name': 'abc'})
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, expected: Dict, mock_org: Mock):
        """Test the org method of GithubOrgClient and
        return value of get_json"""
        mock_org.return_value = expected
        """create an instance of GithubOrgClient with the org_name"""
        obj = GithubOrgClient(org_name)
        """assert that the org property returns the expected result"""
        self.assertEqual(obj.org, expected)
        """Assert that get_json was called once with the expected argument"""
        mock_org.assert_called_once_with(
            'https://api.github.com/orgs/' + org_name)
