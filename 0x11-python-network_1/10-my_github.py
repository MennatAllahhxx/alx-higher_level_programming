#!/usr/bin/python3
"""10-my_github Module"""

import requests
from sys import argv


def my_github():
    """a script to display github id"""

    req = requests.post(url='https://api.github.com/user',
                        auth=(argv[1], argv[2]))

    if req.status_code >= 400:
        print("None")

    else:
        print(req.json().get('id'))


if __name__ == '__main__':
    my_github()
