#!/usr/bin/python3
"""Fetches from https://alx-intranet.hbtn.io/status"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    resp = requests.get(url)
    resp_txt = resp.text
    print('Body response:')
    print(f'\t- type: {type(resp_txt)}')
    print(f'\t- type: {resp_txt}')
