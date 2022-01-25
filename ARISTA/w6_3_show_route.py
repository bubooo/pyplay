#!/usr/bin/env python2

'''
Using your external YAML file and your function located in my_funcs.py, use pyeapi to connect to arista4.lasthop.io and retrieve "show ip route". From this routing table data, extract all of the static and connected routes from the default VRF. Print these routes to the screen and indicate whether the route is a connected route or a static route. In the case of a static route, print the next hop address.
'''

# import modules

import pyeapi
import ipdb
import os
import my_funcs
from getpass import getpass
from pprint import pprint

# Define COSTANTS
PATH = ""
YAML_FILE = "routers.yml"

# Define variable initial value
password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

# Define functions

def main():
    routers = my_funcs.read_yaml(PATH + YAML_FILE)
    # update router's details with password
    for device in routers:
        device["password"] = password
        # we shold do action with aristat4, so that assigned connection details
        if device["host"] == "arista4.lasthop.io":
                device_conn = pyeapi.client.connect(**device)

    device_node = pyeapi.client.Node(device_conn)
    show_route = device_node.enable("show ip route")
    # parse routes and print
    route_table = show_route[0]["result"]["vrfs"]["default"]["routes"]
    ipdb.set_trace()
    for route, route_details  in route_table.items():
        if route_details["directlyConnected"]:
            print(f'{route}\t\t directly connected')
        if route_details["routeType"] == "static":
            print(f'{route}\t\t static \t\t{route_details["vias"][0]["nexthopAddr"]}')
# The CODE
if __name__ == "__main__":
    main()


'''
[{'command': 'show ip route',
  'encoding': 'json',
  'result': {'vrfs': {'default': {'allRoutesProgrammedHardware': True,
                                  'allRoutesProgrammedKernel': True,
                                  'defaultRouteState': 'reachable',
                                  'routes': {'0.0.0.0/0': {'directlyConnected': False,
                                                           'hardwareProgrammed': True,
                                                           'kernelProgrammed': True,
                                                           'metric': 0,
                                                           'preference': 1,
                                                           'routeAction': 'forward',
                                                           'routeType': 'static',
                                                           'vias': [{'interface': 'Vlan1',
                                                                     'nexthopAddr': '10.220.88.1'}]},
                                             '10.220.88.0/24': {'directlyConnected': True,
                                                                'hardwareProgrammed': True,
                                                                'kernelProgrammed': True,
                                                                'routeAction': 'forward',
                                                                'routeType': 'connected',
                                                                'vias': [{'interface': 'Vlan1'}]}},
                                  'routingDisabled': False}}}}]
'''
