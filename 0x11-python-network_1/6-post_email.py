#!/usr/bin/python3
"""Sends a POST request to the URL arg with the email arg as parameter"""

import requests
import sys


if __name__ == '__main__':
    url = sys.arg[1]
    email = sys.arg[2]

    resp = requests.post(url, data={'email': email})
    body = resp.text
    print(body)
