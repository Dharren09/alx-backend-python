#!/usr/bin/env python3


GithubOrgClient = __import__("client").GithubOrgClient

obj = GithubOrgClient("google")
print(obj.org())
