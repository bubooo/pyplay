#!/usr/bin/env python3

'''
Complete the same task as Exercise 1b except this time use "legacy" threads to create a solution. Launch a separate thread for each device's SSH connection. Print the time required to complete the task for all of the devices. Move all of the device specific output printing to the called function (i.e. to the child thread). 

'''

# Import Modules

import time
import threading
import my_devices
import my_functions


# Define CONSTANTS

# Define variable initial values


# Define functions


def main():
    start_time = time.time()
    for device in my_devices.my_devices:
        device_thread = threading.Thread(target = my_functions.ssh_command, args = [device, "show version"])
        device_thread.start()
    
    main_thread = threading.currentThread()
    for thread in threading.enumerate():
        if thread != main_thread:
#            print(thread)
            thread.join()
    end_time = time.time()
    print("It took {:.2f} seconds to complete it.".format(end_time - start_time))  

# THE CODE

if __name__ == "__main__":
    main()
    

