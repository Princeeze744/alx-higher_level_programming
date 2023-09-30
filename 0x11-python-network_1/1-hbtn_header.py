#!/usr/bin/python3
"""Sends request to the URL arg and display the value of the
X-Request-id variable found in the response header"""

import urllib
from urllib import request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as resp:
        req_id = resp.headers.get('X-Request-Id')
        print(req_id)
