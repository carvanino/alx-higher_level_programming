#!/usr/bin/python3
""" 
Send a POST request to the passed URL with an email as a parameter
"""
import urllib.request
import sys

arg = sys.argv
if __name__ == "__main__":
    url = arg[1]
    data = {}
    data['email'] = arg[2]
    url_values = urllib.parse.urlencode(data)
    full_url = url + '?' + url_values
    req = urllib.request.Request(url)
    with urllib.request.urlopen(full_url) as response:
        print(response)

