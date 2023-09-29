#!/bin/bash
#  a Bash script that sends a POST request to the passed URL
curl -sX POST "email: test@gmail.com" -X "subject: I will always be here for PLD" "$1"
