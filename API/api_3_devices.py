#!/usr/bin/env python3

'''
Retrieve a list of all the devices in NetBox. This will require authentication. As in the previous task, create your headers manually and pass them into your request. In order to perform the NetBox authentication, you should do the following:

import os
# Set the token based on the NETBOX_TOKEN environment variable
token = os.environ["NETBOX_TOKEN"]


Then add the following key to your HTTP Headers:

http_headers["Authorization"] = f"Token {token}"


From this returned data structure (the NetBox "/api/dcim/devices/"), print out all of the device "display_names". Note, the response.json() will contain a "results" key. This "results" key will refer to a list of dictionaries. These dictionaries will contain information about each one of the devices in NetBox.


3b. Using the same device information retrieved in exercise 3a, create and print a report to standard output. This report should contain the location, manufacturer, and status for each device. Your output should look similar to the following:

------------------------------------------------------------
arista1
----------
Location: Fremont Data Center
Vendor: Arista
Status: Active
------------------------------------------------------------


------------------------------------------------------------
arista2
----------
Location: Fremont Data Center
Vendor: Arista
Status: Active
------------------------------------------------------------

...   # remaining devices

'''
# import modules
import requests
import os
import ipdb


# Define CONSTANTS

URL = "https://netbox.lasthop.io/api/"

# Define variable initial value

header = {
    "accept": "application/json; version=2.4;"
    }

# Define funcetions

def main():
    token = os.environ["NETBOX_TOKEN"]
    header["Authorization"] = "Token {}".format(token)
    r = requests.get(URL + "dcim/devices", headers = header, verify = False)
    print("These are already defined devices on NetBox:")
    #ipdb.set_trace()
    for device in r.json()["results"]:
        print(device["display_name"])

def report():
    token = os.environ["NETBOX_TOKEN"]
    header["Authorization"] = "Token {}".format(token)
    r = requests.get(URL + "dcim/devices", headers = header, verify = False)
    print("--" *30)
    print("DEVICE REPORT\n")
    for device in r.json()["results"]:
        print(device["display_name"])
        print("-" * 15)
        print(f'Location: {device["site"]["name"]}')
        print(f'Vendor: {device["device_type"]["manufacturer"]["name"]}')
        print(f'Status: {device["status"]["label"]}') 
        print("--" *30 + "\n\n")


# THE CODE

if __name__ == "__main__":
    main()
    report()
