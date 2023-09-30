#!/bin/bash
# Sends a request to the URL passed as argument and displays only the status code
curl -sw %{http_code} "$1" -o /dev/null
