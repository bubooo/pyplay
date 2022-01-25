#! /usr/bin/env python3

'''
Construct a new YAML file that contains the four Arista switches. This YAML file should contain all of the connection information need to create a pyeapi connection using the connect method. Using this inventory information and pyeapi, create a Python script that configures the following on the four Arista switches: 

interface {{ intf_name }}
   ip address {{ intf_ip }}/{{ intf_mask }}

The {{ intf_name }} should be a Loopback interface between 1 and 99 (for example Loopback99).

The {{ intf_ip }} should be an address from the 172.31.X.X address space. The {{ intf_mask }} should be either a /24 or a /30.

Each Arista switch should have a unique loopback number, and a unique interface IP address.

You should use Jinja2 templating to generate the configuration for each Arista switch.

The data for {{ intf_name }} and for {{ intf_ip }} should be stored in your YAML file and should be associated with each individual Arista device. For example, here is what 'arista4' might look like in the YAML file:

​arista4:
  transport: https
  host: arista4.lasthop.io
  username: pyclass
  port: 443
  data:
    intf_name: Loopback99
    intf_ip: 172.31.1.13
    intf_mask: 30


Use pyeapi to push this configuration to the four Arista switches. Use pyeapi and "show ip interface brief" to display the IP address table after the configuration changes have been made.
'''

# import modules
import yaml
import os
import ipdb
import pyeapi
from pprint import pprint
from jinja2.environment import Environment
from jinja2 import FileSystemLoader, StrictUndefined
from getpass import getpass

#define CONSTANTS
TEMPLATE = "iterface_set_ip.j2"
ROUTER_YAML = "routers_4.yml"



# define variable initial values

arista_node = []

# define functions

def main():
    # define password
    password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
    # load router yaml file
    with open(ROUTER_YAML) as y_f:
        routers = yaml.safe_load(y_f)

    # load jinja template
    env = Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader(".")
    template = env.get_template(TEMPLATE)

    #  configure interfaces via API
    for device  in routers:
        #assign passowrd variable to device
        device["password"] = password
        # establis api connction
        connection = pyeapi.client.connect(**device)
        node = pyeapi.client.Node(connection)
        arista_node.append(node)
        # generate config for device using template
        config = template.render(**device["data"])
        #ipdb.set_trace()
        # configure device
        error = node.config(config.splitlines())
        #ipdb.set_trace()
        print(error)

    # Verify interfaces
    for device_node in arista_node:
        show_interfaces = device_node.enable("show ip interface brief")
        hostname = device_node.enable("show hostname")
        print("=-" *30)
        print(hostname[0]["result"]["fqdn"])
        print("--" * 30)
        print(show_interfaces[0]["result"]["output"])
        print("=-" *30)
# THE CODE
if __name__ == "__main__":
    main()
