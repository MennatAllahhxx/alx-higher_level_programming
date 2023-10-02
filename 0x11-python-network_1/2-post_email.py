#!/usr/bin/python3
"""2-post_email Module"""

from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


def post_email():
    """a script to post email"""

    data = {'email': argv[2]}

    req = Request(argv[1], urlencode(data).encode())

    with urlopen(req) as url_response:
        response = url_response.read()
        print(response.decode('UTF-8'))


if __name__ == '__main__':
    post_email()
