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

    def test_public_repos_url(self):
        """Method tests _public_repos_url.
        defining the expected result"""
        expected = "https://api.github.com/orgs/repo"
        """define the payload for the mocked org property"""
        payload = {"repos_url": "https://api.github.com/orgs/repo"}
        with patch('client.GithubOrgClient.org', PropertyMock(
                    return_value=payload)):
            """create an instance of GithugOrgClient"""
            obj = GithubOrgClient("LinkedIn")
            self.assertEqual(obj._public_repos_url, expected)
