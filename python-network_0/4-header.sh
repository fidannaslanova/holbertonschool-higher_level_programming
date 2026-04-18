#!/bin/bash
# Sends a GET request with a header X-School-User-Id: 98
curl -s -H "X-School-User-Id: 98" "$1"
