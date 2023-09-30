#!/usr/bin/python3
"""This script fetches https://alx-intranet.hbtn.io/status"""

import urllib
from urllib import request

if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as resp:
        status = resp.read()
        print('Body response:')
        print(f'\t- type: {type(status)}')
        print(f'\t- content: {status}')
        print(f'\t- utf8 content: {status.decode()}')
