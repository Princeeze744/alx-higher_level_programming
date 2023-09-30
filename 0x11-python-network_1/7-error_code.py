#!/usr/bin/python3
"""Sends a request to the URL arg and displays the body of the response"""

import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    resp = request.get(url)
    body = resp.text
    if resp.status_code > 400:
        print('Error code: {}'.format(resp.status_code))
    else:
        print(body)
