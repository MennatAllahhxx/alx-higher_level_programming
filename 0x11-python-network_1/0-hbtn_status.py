#!/usr/bin/python3
""" 0-hbtn_status Module"""

from urllib.request import urlopen


def fetch_url():
    """ a script to fetch url"""

    with urlopen('https://alx-intranet.hbtn.io/status') as url_response:
        response = url_response.read()
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode("UTF-8")))


if __name__ == '__main__':
    fetch_url()
