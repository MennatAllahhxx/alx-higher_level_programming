#!/usr/bin/python3
"""1-hbtn_header Module"""

from urllib.request import urlopen
from sys import argv


def fetch_item_from_url():
    """a script to fetch item"""

    with urlopen(argv[1]) as url_response:
        print(url_response.getheader("X-Request-Id"))


if __name__ == '__main__':
    fetch_item_from_url()
