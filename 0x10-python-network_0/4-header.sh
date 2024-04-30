#!/bin/bash
# This Bash script takes in a URL as an argument, sends a GET request to the URL with a header X-School-User-Id: 98, and displays the body of the response
curl -sH "X-School-User-Id: 98" $1
