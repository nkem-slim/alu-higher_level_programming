#!/usr/bin/python3
"""
A Python script that fetches http://0.0.0.0:5050/status

"""


import urllib.request
with urllib.request.urlopen('http://0.0.0.0:5050/status') as response:
    retrieved = response.read()

print("Body response:")
print("\t- type: {}".format(type(retrieved)))
print("\t- content: {}".format(retrieved))
print("\t- utf8 content: {}".format(retrieved.decode('utf-8')))
