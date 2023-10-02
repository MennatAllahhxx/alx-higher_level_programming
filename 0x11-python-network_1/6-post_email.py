#!/usr/bin/python3
"""6-post_email Module"""

import requests
from sys import argv


def post_email():
    """a script to post email"""

    data = {'email': argv[2]}
    req = requests.post(argv[1], data)
    print(req.text)


if __name__ == '__main__':
    post_email()
