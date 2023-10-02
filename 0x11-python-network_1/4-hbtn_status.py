#!/usr/bin/python3
"""4-hbtn_status Module"""

import requests


def fetch_url():
    """ a script to fetch url"""

    response = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == '__main__':
    fetch_url()
