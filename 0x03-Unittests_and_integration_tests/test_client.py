#!/usr/bin/env python3

import unittest
from unittest.mock import patch, Mock, PropertyMock, call
from parameterized import parameterized, parameterized_class
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

    @patch("client.get_json")
    def test_public_repos(self, mock_obj: Mock):
        """Method tests property _public_repos.
        define the expected result for the mocked get_json function"""
        expected = {"Command": "git_push"}
        """configure the mock object to return the expected result"""
        mock_obj.return_value = expected

        """Define the expected result for the mocked
        public_repos_url property"""
        result = "github.com/LinkedIn"

        """Patch the _public_repos_url property of GithubOrgClient
        with a PropertyMock"""
        with patch("client.GithubOrgClient._public_repos_url", PropertyMock(
                return_value=result)) as mock_repo:
            """create an instance of GithubOrgClient"""
            obj = GithubOrgClient("LinkedIn")
            self.assertEqual(obj._public_repos_url, result)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict[str, Dict],
                         license_key: str, expected: bool):
        """tests license"""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Implement intergration test for public_repos method"""

    @classmethod
    def setUpClass(cls):
        """Prepare to test, Extract the neccessary payloads
        from TEST_PAYLOAD"""
        org = TEST_PAYLOAD[0][0]
        repos = TEST_PAYLOAD[0][1]

        """Create mock objects for org and repos payloads"""
        org_mock = Mock()
        org_mock.json = Mock(return_value=org)
        cls.org_mock = org_mock

        repos_mock = Mock()
        repos_mock.json = Mock(return_value=repos)
        cls.repos_mock = repos_mock

        """Patch the 'requests.get' function to return the
        appropriate mock objects"""
        cls.get_patcher = patch('requests.get')
        cls.get = cls.get_patcher.start()
        options = {cls.org_payload["repos_url"]: repos_mock}
        cls.get.side_effect = lambda y: options.get(y, org_mock)

    @classmethod
    def tearDownClass(cls):
        """ unprepare for testing """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ public repos test, create an instance of GithubOrgClient """
        y = GithubOrgClient("x")

        """Assert the org payload, repos payload, and expected repos"""
        self.assertEqual(y.org, self.org_payload)
        self.assertEqual(y.repos_payload, self.repos_payload)
        self.assertEqual(y.public_repos(), self.expected_repos)
        self.assertEqual(y.public_repos("NONEXISTENT"), [])

        """Assert the calls made to requests.get"""
        self.get.assert_has_calls([call("https://api.github.com/orgs/x"),
                                   call(self.org_payload["repos_url"])])

    def test_public_repos_with_license(self):
        """ public repos test """
        y = GithubOrgClient("x")

        """Assert the org payload, repos payload, and expected repos"""
        self.assertEqual(y.org, self.org_payload)
        self.assertEqual(y.repos_payload, self.repos_payload)
        self.assertEqual(y.public_repos(), self.expected_repos)
        self.assertEqual(y.public_repos("NONEXISTENT"), [])
        self.assertEqual(y.public_repos("apache-2.0"), self.apache2_repos)

        """Assert the calls made to requests.get"""
        self.get.assert_has_calls([call("https://api.github.com/orgs/x"),
                                   call(self.org_payload["repos_url"])])


if __name__ == '__main__':
    unittest.main()
