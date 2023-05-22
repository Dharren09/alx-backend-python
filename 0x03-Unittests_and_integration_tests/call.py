#!/usr/bin/env python3

import requests
import json

response = requests.get("https://api.github.com/orgs/abc")
print(response.json())
