#!/usr/bin/env python3

'''
In your lab environment, there is a file located at ~/.netmiko.yml. This file contains all of the devices used in the lab. Create a Python program that processes this YAML file and then uses Netmiko to connect to the Cisco3 router. Print out the router prompt from this device.

Note, the device dictionaries in the .netmiko.yml file use key-value pairs designed to work directly with Netmiko. The .netmiko.yml also contains group definitions for: cisco, arista, juniper, and nxos groups. These group definitions are lists of devices. Once again, don't check the .netmiko.yml into GitHub.
'''

# import modules
import yaml
from netmiko import ConnectHandler

# define variable initial value

# define CONSTANTS
FILE = "/home/bucko/.netmiko.yml"


if __name__ == "__main__":
    with open(FILE) as f:
        routers = yaml.load(f)

    with ConnectHandler(**routers["cisco3"]) as session:
        prompt = session.find_prompt()

    print(prompt)
