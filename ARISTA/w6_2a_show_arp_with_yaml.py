#!/usr/bin/env python3

'''
2a. Define an Arista device in an external YAML file (use arista4.lasthop.io for the device). In your YAML file, make sure the key names exactly match the names required for use with pyeapi and the connect() method. In other words, you should be able to execute 'connect(**device_dict)' where device_dict was retrieved from your YAML file. Do not store the lab password in this YAML file, instead set the password using getpass() in your Python program. Using this Arista device information stored in a YAML file, repeat the 'show ip arp' retrieval using pyeapi. Once again, from this ARP table data, print out a mapping of all of the IP addresses and their corresponding MAC addresses.
'''

# IMport modules
import yaml
import pyeapi
import os
import ipdb
from getpass import getpass

# Define CONSTANTS
PATH = ""
ROUTER_DETAILS = "routers.yml"

# Define variable initial values

password =  os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

# Define functions

def main():
    with open(PATH + ROUTER_DETAILS) as f:
        routers_details = yaml.safe_load(f)
    #ipdb.set_trace()
    # update yaml data with password response
    for router_item in routers_details:
        router_item["password"] = password

    #ipdb.set_trace()
    device_conn = pyeapi.client.connect(**routers_details[0])
    device_node = pyeapi.client.Node(device_conn)
    show_arp = device_node.enable("show ip arp")
    #print arp table
    print("Device ARP table:")
    print("=-" *30)
    #ipdb.set_trace()
    for entry in show_arp[0]["result"]["ipV4Neighbors"]:
        print(f'{entry["address"]}\t:\t{entry["hwAddress"]}')

if __name__ == "__main__":
    main()
