#!/usr/bin/python3
"""Script takes in my credentials (username and password)
and uses the GitHub API passed as argument to the script"""

import requests
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'

    req = requests.Request(
            'GET',
            url,
            auth=(username, password),
            headers={'User-Agent': 'Python-Script'})
    prep_req = req.prepare()
    s = requests.Session()
    resp = s.send(prep_req)

    if resp.status_code >= 400:
        print('None')
    else:
        github_id = resp.json().get('id')
        print(github_id)
