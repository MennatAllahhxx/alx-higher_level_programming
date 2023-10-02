#!/usr/bin/python3
"""5-hbtn_header Module"""

import requests
from sys import argv


def fetch_item_from_url():
    """a script to fetch item"""

    url_response = requests.get(argv[1])
    print(url_response.headers.get("X-Request-Id"))


if __name__ == '__main__':
    fetch_item_from_url()
