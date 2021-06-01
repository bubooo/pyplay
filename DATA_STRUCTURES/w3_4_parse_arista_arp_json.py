#!/usr/bin/env python3
'''
You have the following JSON ARP data from an Arista switch: arista_arp.json
From a file, read this JSON data into your Python program. Process this ARP data and return a dictionary where the dictionary keys are the IP addresses and the dictionary values are the MAC addresses. Print this dictionary to standard output.
'''

# import modules
from pprint import pprint
import json


# define variable initial value
ip_mac_add_dict = {}


if __name__ == "__main__":
    with open("arista_arp.json") as file:
        arp_data = json.load(file)

    for arp_entries_dict in arp_data["ipV4Neighbors"]:
        ip_mac_add_dict.update({arp_entries_dict["address"]:arp_entries_dict["hwAddress"]})

    print("ARP table:\n")
    print("_" *20)
    pprint(ip_mac_add_dict)
