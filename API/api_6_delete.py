#!/usr/bin/env python3

'''
6. Use an HTTP DELETE and Python-requests to delete the IP address object that you just created. Remember to reference the ID of your object.
'''


# import modules
import requests
import os
import json
from pprint import pprint
import ipdb

# Define CONSTANTS
URL = "https://netbox.lasthop.io/api/"

# Define variable initial value

header = {}


address_id = input("Zadaj IP address ID, ktore ZMAZAT:")

# Define function

def main():
    header["accept"] = "application/json; version=2.4;"
    header["Authorization"] = f'Token {os.environ["NETBOX_TOKEN"]}'
    header["Content-Type"] = "application/json; version=2.4;"

    #r = requests.put(URL + "ipam/ip-addresses/" + "443/", headers = header, data = json.dumps(data), verify = False)
    r = requests.delete(f'{URL}ipam/ip-addresses/{address_id}/', headers = header, verify = False)
    print("Request status code: {}".format(r.status_code))
    #ipdb.set_trace()

# THE CODE

if __name__ == "__main__":
    main()
