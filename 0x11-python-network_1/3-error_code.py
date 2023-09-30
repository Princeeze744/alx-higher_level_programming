#!/usr/bin/python3
"""Sends a request to the URL arg and displays the body of the response"""

import urllib
import sys
from urllib import request, error

if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as err:
        print('Error code: {}'.format(err.code))
