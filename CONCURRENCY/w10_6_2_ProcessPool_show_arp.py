#!/usr/bin/env python3

'''
Using a context manager, the ProcessPoolExecutor, and the map() method, create a solution that executes "show ip arp" on all of the devices defined in my_devices.py. Note, the Juniper device will require "show arp" instead of "show ip arp" so your solution will have to properly account for this.
'''

# import modules
from concurrent.futures import ProcessPoolExecutor, as_completed
from my_devices import my_devices
from my_functions import ssh_command2
import time
import ipdb 


# define CONSTANTS

# define variable intial values
pool_size = 4
threads = []
devices_juniper = []
devices_other = []
commands = []
# define functions

def main():
    for device in my_devices:
        if "juniper" in device["device_type"]:
            commands.append("show arp")
        else:
            commands.append("show ip arp")
    start_time = time.time()
    with ProcessPoolExecutor(pool_size) as pool:
        futures_output = pool.map(ssh_command2, my_devices, commands)

        # print outputs
#        ipdb.set_trace()
        for result in futures_output:
            print("=-"*30)
            print("Result:\n{}".format(result))
            print("\n\n")
        print("Elapsed time: {}".format(time.time() - start_time))
# THE CODE

if __name__ == "__main__":
    main()
