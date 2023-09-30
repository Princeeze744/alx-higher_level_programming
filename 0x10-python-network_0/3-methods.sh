#!/bin/bash
# Scropt displays all HTTP methods allowed by the server
curl -sI "$1" | grep Allow | cut -b8-
