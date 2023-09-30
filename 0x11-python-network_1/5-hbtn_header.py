#!/usr/bin/python3
"""Sends request to URL arg and displays the value of the variable
X-Request-Id in the response header"""

import requests
import sys

if __name__ == '__main__':
    url = sys.arg[1]
    resp = requests.get(url)
    header_var = resp.headers.get('X-Request-Id')
    print(header_var)
