#!/usr/bin/env python3
'''
For one of the Cisco IOS devices, use Netmiko and the send_command() method to retrieve 'show version'. Save this output to a file in the current working directory.
'''

#Define viariable initial value
router = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "global_delay_factor": 3,
    "device_type": "cisco_ios",
    "session_log": "session.log",
    }

#Define CONSTANTS
PATH = ""
FILE = "cisco3_show_version.txt"
#import libraries
from netmiko import ConnectHandler

if __name__ == "__main__":
    router_session = ConnectHandler(**router)
    show_version_output = router_session.send_command("show version",strip_command=False,strip_prompt=False)
    with open(PATH+FILE,"w") as output_file:
        write_confirm = output_file.write(show_version_output) 
    print("written {} bytes".format(write_confirm))
