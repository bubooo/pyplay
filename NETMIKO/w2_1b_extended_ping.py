#!/usr/bin/env python3
'''
 Use the extended 'ping' command and Netmiko on the 'cisco4' router. This should prompt you for additional information as follows:

cisco4#ping
Protocol [ip]: 
Target IP address: 8.8.8.8
Repeat count [5]: 
Datagram size [100]: 
Timeout in seconds [2]: 
Extended commands [n]: 
Sweep range of sizes [n]: 
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/4 ms

a. Use send_command_timing() to handle the additional prompting from this 'ping' command. Specify a target IP address of '8.8.8.8'

b. Use send_command() and the expect_string argument to handle the additional prompting. Once again specify a target IP address of '8.8.8.8'.
'''

#Define variable initial value
router = "cisco4"

#Define CONSTANTS
DESTINATION = "8.8.8.8"
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
#    print("cisco4 router is {}. item in list and iths FQDN is: {}".format(routers_index,device_list["routers"][routers_index]["host"]))

    
    with ConnectHandler(**device_list["routers"][routers_index]) as router_session:
        output = router_session.send_command("ping",expect_string=r'Protocol', strip_command=False)
        output += router_session.send_command("\n", expect_string=r'Target', strip_command=False)
        output += router_session.send_command(DESTINATION, expect_string=r'Repeat count', strip_command=False)
        for i in range(5):
               output += router_session.send_command("\n", expect_string=r'.*', strip_command=False)
        print(output)


