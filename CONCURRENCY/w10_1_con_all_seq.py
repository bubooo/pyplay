#!/usr/bin/env python3

'''
1a. As you have done in previous classes, create a Python file named "my_devices.py". In this file, define the connection information for: 'cisco3', 'arista1', 'arista2', and 'srx2'. This file should contain all the necessary information to create a Netmiko connection. Use getpass() for the password handling. Use a global_delay_factor of 4 for both the arista1 device and the arista2 device. This Python module should be used to store the connection information for all of the exercises in this lesson.

1b. Create a Python script that executes "show version" on each of the network devices defined in my_devices.py. This script should execute serially i.e. one SSH connection after the other. Record the total execution time for the script. Print the "show version" output and the total execution time to standard output. As part of this exercise, you should create a function that both establishes a Netmiko connection and that executes a single show command that you pass in as argument. This function's arguments should be the Netmiko device dictionary and the "show-command" argument. The function should return the result from the show command.
'''

# Import modules
from netmiko import ConnectHandler
import time
from my_devices import my_devices



# Define CONSTATNTS


# Define variable initial values



# Define functions
def nw_get_show(device, command):
    connection = ConnectHandler(**device)
    output = connection.send_command(command)
    connection.disconnect()
    return output

def main():   
    start_time = time.time()
    print("=-" *30 + "\n\n")
    for router in my_devices:
        result = nw_get_show(router, "show version")
        print("{} router version:\n{}".format(router["host"], result))
        print("=-" *30 + "\n\n")
    end_time = time.time()
    print("Elapsed time in seconds: {:.2f}".format(end_time - start_time))
    print("=-" *30 + "\n\n")



# THE CODE
if __name__ == "__main__":
    main()
