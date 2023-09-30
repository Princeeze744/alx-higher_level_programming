#!/bin/bash
# Script takes in a URL arg, sends a request to the URL and displays the size of the body of the response
curl -sI "$1" | grep Content-Length | cut -d' ' -f2
