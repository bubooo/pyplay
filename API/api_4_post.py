#!/usr/bin/env python3

'''
4a. Using an HTTP POST and the Python-requests library, create a new IP address in NetBox. This IP address object should be a /32 from the 192.0.2.0/24 documentation block. Print out the status code and the returned JSON.

The HTTP headers for this request should look as follows:

http_headers = {}
http_headers["Content-Type"] = "application/json; version=2.4;"
http_headers["accept"] = "application/json; version=2.4;"
http_headers["Authorization"] = f"Token {token}"


The URL for the HTTP POST is:

https://netbox.lasthop.io/api/ipam/ip-addresses/


The JSON payload data for this request should be similar to the following:

data = {"address": "192.0.2.100/32"}


4b. Using the response data from the HTTP POST that created the IP address entry in exercise 4a, capture the "id" of the newly created IP address object. Using this ID, construct a new URL. Use this new URL and the HTTP GET method to retrieve only the API information specific to this IP address. Your IP address URL should be of the following form:

https://netbox.lasthop.io/api/ipam/ip-addresses/{address_id}/


where {address_id} is the ID of the object that you just created.

Pretty print the response.json() data from this HTTP GET. Please note the ID of the address object that you just created.
'''

# import modules
import requests
import os
import json
from pprint import pprint

# Define CONSTANTS
URL = "https://netbox.lasthop.io/api/"

# Define variable initial value

header = {}

data = {
    "address": "192.0.2.100/32"
    }

# Define function

def main():
    header["accept"] = "application/json; version=2.4;"
    header["Authorization"] = f'Token {os.environ["NETBOX_TOKEN"]}'
    header["Content-Type"] = "application/json; version=2.4;"

    r = requests.post(URL + "ipam/ip-addresses/", headers = header, data = json.dumps(data), verify = False)
    print("Request status code: {}".format(r.status_code))
    print("Request message response:")
    pprint(r.json())

    # 4b
    print("=-=" * 20)
    ch = requests.get(URL + "ipam/ip-addresses/" + str(r.json()["id"]), headers = header, verify = False)
    print("Check request status code: {}".format(ch.status_code))
    print("Check request message response:")
    pprint(ch.json())
# THE CODE

if __name__ == "__main__":
    main()
