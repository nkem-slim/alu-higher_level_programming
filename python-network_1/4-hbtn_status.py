#!/usr/bin/python3
"""
Python script that fetches https://alu-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests

    retrieved = requests.get('https://alu-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(retrieved.text)))
    print("\t- content: {}".format(retrieved.text))
