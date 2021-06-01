#!usr/bin/env python3

'''
Use Netmiko to retrieve 'show run' from the Cisco4 device. Feed this configuration into CiscoConfParse.

Use CiscoConfParse to find all of the interfaces on Cisco4 that have an IP address. Print out the interface name and IP address for each interface. Your solution should work if there is more than one IP address configured on Cisco4. For example, if you configure a loopback interface on Cisco4 with an IP address, then your solution should continue to work. The output from this program should look similar to the following:

$ python confparse_ex6.py 

Interface Line: interface GigabitEthernet0/0/0
IP Address Line:  ip address 10.220.88.23 255.255.255.0
'''

# import modules
import re
import yaml
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse


# define CONSTANTS
PATH = "/home/bucko"
FILE = ".netmiko.yml"

# define variable initial value



if __name__ == "__main__":
    with open(PATH + "/" + FILE) as f:
        routers = yaml.load(f)
    with ConnectHandler(**routers["cisco4"]) as cisco4:
        cisco4_config = cisco4.send_command("show configuration", expect_string=r'#')

    #cisco4_config_list = cisco4_config.splitlines()
    cisco4_conf_parse = CiscoConfParse(cisco4_config.splitlines())
    interfaces_w_ip = cisco4_conf_parse.find_objects_w_child(parentspec=r'^interface', childspec=r'^\s+ip address')
    for parent in interfaces_w_ip:
        print("\nInterface Line: {}\n".format(parent.text))
        print("IP Address Line: {}\n".format(parent.re_search_children(r'^\s+ip address').text))
    
