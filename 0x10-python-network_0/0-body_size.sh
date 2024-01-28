#!/usr/bin/env bash
# Get the number of bytes of the HTTP response header from a URL
curl -s "$1" | wc -c
