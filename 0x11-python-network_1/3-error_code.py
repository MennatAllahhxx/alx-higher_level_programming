#!/usr/bin/python3
"""3-error_code Module"""

from urllib.request import urlopen, Request
from urllib.error import HTTPError
from sys import argv


def find_error():
    """a script to find error"""

    # req = Request(argv[1])

    try:
        with urlopen(argv) as url_response:
            response = url_response.read()
            print(response.decode('UTF-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == '__main__':
    find_error()
