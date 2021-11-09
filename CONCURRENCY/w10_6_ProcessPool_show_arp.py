#!/usr/bin/env python3

'''
Using a context manager, the ProcessPoolExecutor, and the map() method, create a solution that executes "show ip arp" on all of the devices defined in my_devices.py. Note, the Juniper device will require "show arp" instead of "show ip arp" so your solution will have to properly account for this.
'''

# import modules
from concurrent.futures import ProcessPoolExecutor, as_completed
from my_devices import my_devices
from my_functions import ssh_command2
from itertools import repeat
import time
import ipdb 


# define CONSTANTS

# define variable intial values
pool_size = 4
threads = []
devices_juniper = []
devices_other = []
# define functions

def main():
    for device in my_devices:
        if device["device_type"] == "juniper_junos":
            devices_juniper.append(device)
        else:
            devices_other.append(device)
    start_time = time.time()
    with ProcessPoolExecutor(pool_size) as pool:
        # repeat() is required to repeat argument as .map require iterable
        # list() is required to transform map output, generator, to list, because can't 'generator'+'generator'
        futures_rest = list(pool.map(ssh_command2, devices_other, repeat("show ip arp")))
        futures_juniper = list(pool.map(ssh_command2, devices_juniper, repeat("show arp")))

        # print outputs
#        ipdb.set_trace()
        for result in (futures_rest + futures_juniper):
            print("=-"*30)
            print("Result:\n{}".format(result))
            print("\n\n")
        print("Elapsed time: {}".format(time.time() - start_time))
# THE CODE

if __name__ == "__main__":
    main()
