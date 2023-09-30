#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with
the arg passed as parameter"""

import requests
import sys


if __name__ == '__main__':
    q = ''
    if len(sys.argv) > 1:
        q = sys.argv[1]
    url = 'http://0.0.0.0:5000/search_user'

    resp = requests.post(url, data={'q': q})
    try:
        if not resp.json():
            print('No result')
        else:
            json_res = resp.json()
            print('[{)] {}'.format(json_res.get('id'), json_res.get('name')))
    except Exception:
        print('Not a valid JSON')
