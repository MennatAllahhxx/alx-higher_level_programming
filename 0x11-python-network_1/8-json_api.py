#!/usr/bin/python3
"""8-json_api Module"""

import requests
from sys import argv


def post_letter():
    """a script to post a letter"""

    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""

    data = {'q': q}
    req = requests.get('http://0.0.0.0:5000/search_user', data)

    try:
        req_json = req.json()

        if not req_json:
            print("No result")

        else:
            id = req_json.get('id')
            name = req_json.get('name')
            print("[{}] {}".format(id, name))

    except ValueError:
        print("Not a valid JSON")


if __name__ == '__main__':
    post_letter()
