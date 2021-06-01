#!/usr/bin/env python3

'''
Read this JSON data in from a file.

From this data structure extract all of the IPv4 and IPv6 addresses that are used on this NXOS device. From this data create two lists: 'ipv4_list' and 'ipv6_list'. The 'ipv4_list' should be a list of all of the IPv4 addresses including prefixes; the 'ipv6_list' should be a list of all of the IPv6 addresses including prefixes.
'''

# import modules
import json
from pprint import pprint

# define variables initial value
ipv4_add = []
ipv6_add = []


if __name__ == "__main__":
    with open("nxos_interfaces.json") as j_file:
        nxos_interfaces = json.load(j_file)

    for _, interface in nxos_interfaces.items():
        for ip_type, address_dict in interface.items():
            for ip_address, prefix_dict in address_dict.items():
                if ip_type == "ipv4":
                    ipv4_add.append("{}/{}".format(ip_address,prefix_dict["prefix_length"]))
                else:
                    ipv6_add.append("{}/{}address".format(ip_address,prefix_dict["prefix_length"]))


    print("These are IPv4 addresses")
    print("="*20)
    pprint(ipv4_add)
    print("-"*20)
    print("These are IPV6 used addresses")
    print("="*20)
    pprint(ipv6_add)


