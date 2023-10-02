#!/usr/bin/python3
"""7-error_code Module"""

import requests
from sys import argv


def find_error():
    """a script to find error"""

    try:
        req = requests.get(argv[1])
        req.raise_for_status()
        print(req.text)

    except requests.exceptions.HTTPError:
        print("Error code: {}".format(req.status_code))


if __name__ == '__main__':
    find_error()
