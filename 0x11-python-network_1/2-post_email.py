#!/usr/bin/python3
"""Sends a POST request to the URL arg with the email arg as a parameter
and display the body of the response"""

import urllib
import sys
from urllib import request, parse


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as resp:
        body = resp.read()
        body = body.decode('utf-8')
        print(body)
