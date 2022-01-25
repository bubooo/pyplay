#!/usr/bin/env pyhton3

'''
Using the pyeapi library, connect to arista3.lasthop.io and execute 'show ip arp'. From this ARP table data, print out a mapping of all of the IP addresses and their corresponding MAC addresses.
'''

# import modules
import pyeapi
from getpass import getpass
import ipdb

# Define CONSTANTS

# Define variable initial value
arista3_details = {
                    "host": "arista3.lasthop.io",
                    "transport": "https",
                    "username": "pyclass",
                    "password": getpass(),
                    "port": "443"
                    }




# Define functions
def main():
    arista_connection = pyeapi.client.connect(**arista3_details)
    #ipdb.set_trace()
    arista_node = pyeapi.client.Node(arista_connection, enablepwd = arista3_details["password"])
    show_arp = arista_node.enable("show ip arp")

    #print arp table
    print("Arista3 ARP table:")
    print("=-" *30)
    #ipdb.set_trace()
    for entry in show_arp[0]["result"]["ipV4Neighbors"]:
        print(f'{entry["address"]}\t:\t{entry["hwAddress"]}')


# THE CODE
if __name__ == "__main__":
    main()
