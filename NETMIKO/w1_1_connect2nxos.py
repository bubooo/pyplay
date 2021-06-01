#!/usr/bin/env python3
'''
In the lab environment use Netmiko to connect to one of the Cisco NX-OS devices. You can find the IP addresses and username/passwords of the Cisco devices in the 'Lab Environment' email or alternatively in the ~/.netmiko.yml file. Simply print the router prompt back from this device to verify you are connecting to the device properly.
'''

from netmiko import ConnectHandler
from getpass import getpass

#Define variable initial values
router = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_nxos"
}

#Define CONSTATS

if __name__ == "__main__":
    router_session = ConnectHandler(**router)
    print("This is router with hostname {}".format(router_session.find_prompt()))
