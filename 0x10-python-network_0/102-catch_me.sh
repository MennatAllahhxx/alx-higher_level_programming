#!/bin/bash
#a Bash script that makes a request to 0.0.0.0:5000/catch_me
curl -sLX PUT -H "Origin: School" http://0.0.0.0:5000/catch_me
