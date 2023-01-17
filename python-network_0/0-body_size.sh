#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the respons
curl -sI "$1" | grep -E 'Content-Length' | cut -d ' ' -f 2
