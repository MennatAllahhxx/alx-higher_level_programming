#!/usr/bin/python3
"""100-github_commits Module"""

import requests
from sys import argv


def github_repo_commits():
    """a script to display github last 10 commits"""

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    commits = requests.get(url=url).json()

    for commit in commits[:10]:
        print("{}: {}".format(commit.get('sha'),
                              commit.get('commit').get('author').get('name')
                              )
              )


if __name__ == '__main__':
    github_repo_commits()
