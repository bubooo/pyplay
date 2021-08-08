#!/usr/bin/env python3
'''
Create a Netmiko connection to the 'nxos2' device using a global_delay_factor of 2. Execute 'show lldp neighbors detail' and print the returned output to standard output. Execute 'show lldp neighbors detail' a second time using send_command() with a delay_factor of 8. Print the output of this command to standard output. Use the Python datetime library to record the execution time of both of these commands. Print these execution times to standard output.
'''

#Define variable initial value
router = "nxos2"

#Define CONSTANTS
CMD = "show lldp neighbors detail"
ROUTERS_FILE = "routers.json"
PATH = "/home/bucko"
#Import modules
import json
from netmiko import ConnectHandler

if __name__ == "__main__":
    with open(PATH+"/"+ROUTERS_FILE) as json_f:
        device_list = json.load (json_f)
    
# Find device's index
    for device_index,routers_dict in enumerate(device_list["routers"]):
        if router in routers_dict["host"]:   
            routers_index = device_index
            break
# connect to device
    with ConnectHandler(**device_list["routers"][routers_index], global_delay_factor=2) as router_session:
        # send commands
        output = device_list["routers"][routers_index]["host"] + " LLDP neighbors:\n"
        output += router_session.send_command(CMD + "\n", strip_prompt=False, strip_command=False)
        output += device_list["routers"][routers_index]["host"] + " LLDP neighbor with delay factor 8+2=10 sec:\n"
        output += router_session.send_command(CMD + "\n", strip_prompt=False, strip_command=False, delay_factor=8)
        print(output)


