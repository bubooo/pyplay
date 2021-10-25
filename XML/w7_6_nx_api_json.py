#!/usr/bin/env python3

''''
6a. Create an nxapi_plumbing "Device" object for nxos1. The api_format should be "jsonrpc" and the transport should be "https" (port 8443). Use getpass() to capture the device's password. Send the "show interface Ethernet1/1" command to the device, parse the output, and print out the following information:

Interface: Ethernet1/1; State: up; MTU: 1500


'''

# import modules
from nxapi_plumbing import Device
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning 
from getpass import getpass

# Define CONSTANTS

NXOS1 = {
    "api_format":"jsonrpc",
    "host":"nxos1.lasthop.io",
    "username":"pyclass",
    "password":getpass(),
    "transport":"https",
    "port":"8443",
    "verify":False,
    }


# Define variable initial values



#Define functions


# The CODE

if __name__ == "__main__":
    nxos1_conn = Device(**NXOS1)
    interface_show = nxos1_conn.show("show interface Ethernet1/1") 
    eth1_1 = interface_show["TABLE_interface"]["ROW_interface"]
    print("+=" *30)
    print("Interface: {}; State: {}; MTU: {}".format(eth1_1["interface"], eth1_1["state"], eth1_1["eth_mtu"]))
    print("+=" *30)
