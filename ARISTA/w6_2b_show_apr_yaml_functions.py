#!/usb/bin/env python3

'''
Create a Python module named 'my_funcs.py'. In this file create two functions: function1 should read the YAML file you created in exercise 2a and return the corresponding data structure; function2 should handle the output printing of the ARP entries (in other words, create a separate function that handles all printing to standard out of the 'show ip arp' data). Create a new Python program based on exercise2a except the YAML file loading and the output printing is accomplished using the functions defined in my_funcs.py.
'''

# Import modules
import yaml
import pyeapi
import ipdb
import my_funcs
import os
from getpass import getpass

# Define CONSTANTS

FILE = "routers.yml"
PATH = ""

# Define varaible initial values
password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
# define functions

def main():
    routers_yaml = my_funcs.read_yaml(PATH + FILE)
    for router in routers_yaml:
        router["password"] = password

    device_conn = pyeapi.client.connect(**routers_yaml[0])
    device_node = pyeapi.client.Node(device_conn)
    show_arp = device_node.enable("show ip arp")

    my_funcs.print_arp(show_arp)
# THE CODE

if __name__ == "__main__":
    main()
