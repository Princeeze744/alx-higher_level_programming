#!/bin/bash
# Script sends a custom header variable in a GET request to the URL arg
curl -s -X GET -H "X-School-User-Id: 98" "$1"
