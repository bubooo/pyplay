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

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
# Define CONSTANTS

HEADER = {}
URL = "https://netbox.lasthop.io/api/"

# Define variable initial values

# Define functions

def main():
    response = requests.get(URL, verify = False)
    print("Response status code: {}".format(response.status_code))
    print("Response header:\n{}".format(response.headers))
    print("==" * 30)
    print("Response test:\n{}".format(response.text))
    print("=-" * 30)
    print("Response in JSON:\n{}".format(response.json()))


# THE CODE

if __name__ == "__main__":
    main()


