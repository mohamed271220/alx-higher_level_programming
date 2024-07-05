#!/bin/bash
# This script takes in a URL, sends a request to that URL, an
curl -s "${1}" | wc -c