#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests

    retrieved = requests.get('https://0.0.0.0:5050/status')
    print("Body response:")
    print("\t- type: {}".format(type(retrieved.text)))
    print("\t- content: {}".format(retrieved.text))
