#!/usr/bin/python3
"""100-github_commits Module"""

import requests
from sys import argv


def github_repo_commits():
    """a script to display github last 10 commits"""

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    req = requests.get(url=url).json()

    try:
        for i in range(10):
            print("{}: {}".format(req[i]["sha"],
                                  req[i]["author"]["name"]
                                  )
                  )
    except Exception:
        pass


if __name__ == '__main__':
    github_repo_commits()
