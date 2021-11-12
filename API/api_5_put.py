#!/usr/bin/env python3

'''
5. Building on the script from exercise 4, add a description to the the IP address object that you just created. Accomplish this using an HTTP PUT. The HTTP PUT operation will require all of the mandatory fields in the object (in this case, the "address" field). Print the status code and the response.json() from your PUT operation. The HTTP PUT operation will use same URL as exercise 4b (i.e. the URL of the newly created IP address object including its ID).
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

data = {
    "address": "192.0.2.100/32",
    "description": "Toto je NAKA adresa"
    }

address_id = input("Zadaj IP address ID, ktore updatnut:")

# Define function

def main():
    header["accept"] = "application/json; version=2.4;"
    header["Authorization"] = f'Token {os.environ["NETBOX_TOKEN"]}'
    header["Content-Type"] = "application/json; version=2.4;"

    #r = requests.put(URL + "ipam/ip-addresses/" + "443/", headers = header, data = json.dumps(data), verify = False)
    r = requests.put(f'{URL}ipam/ip-addresses/{address_id}/', headers = header, data = json.dumps(data), verify = False)
    print("Request status code: {}".format(r.status_code))
    print("Request message response:")
    #ipdb.set_trace()
    pprint(r.json())

# THE CODE

if __name__ == "__main__":
    main()
