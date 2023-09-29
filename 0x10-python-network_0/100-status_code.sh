#!/bin/bash
#a Bash script that displays a Bash script that displays
curl -LI "$1" -o /dev/null -w '%{http_code}' -s
