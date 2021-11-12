#!/usr/bin/env python3

'''
Using the Python requests library, perform an HTTP GET on the base URL of the NetBox server (https://netbox.lasthop.io/api/). Ensure that you are not verifying the SSL certificate. Print the HTTP status code, the response text, the JSON response, and the HTTP response headers. These items can be accessed using the following attributes/methods in the Python-requests Response object:

response.status_code
response.text
response.json()
response.headers



'''
# Import modules
import requests
from urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
import ipdb

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
# Define CONSTANTS

URL = "https://netbox.lasthop.io/api/"

# Define variable initial values
header = {
        "accept": "application/json; version=2.4"
        }

# Define functions

def main():
    response = requests.get(URL,headers = header, verify = False)
    print("Response status code: {}".format(response.status_code))
    print("Response header:\n{}".format(response.headers))
    print("==" * 30)
    print("Response test:\n{}".format(response.text))
    print("=-" * 30)
    print("Response in JSON:\n{}".format(response.json()))

# 2c dcim endpoints
def dcim():
    r = requests.get(URL + "dcim", headers = header, verify = False)
    print("API \"dcim\" Netbox categories:")
    print("== " * 30 ) 
    pprint(r.json())
    print("== " * 30 ) 
    print(type(r.json()))
    #ipdb.set_trace()
    print(f"Use following URL for device type querys: {r.json()['device-types']}")
    

# THE CODE

if __name__ == "__main__":
    main()
    dcim()

