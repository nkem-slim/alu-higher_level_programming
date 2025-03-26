#!/usr/bin/python3
"""
A Python script that fetches https://alu-intranet.hbtn.io/status

"""


import urllib.request
with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
    retrieved = response.read()

print("Body response:")
print("\t- type: {}".format(type(retrived)))
print("\t- content: {}".format(retrieved))
print("\t- utf8 content: {}".format(retrieved.decode('utf-8')))
