#!/usr/bin/env python3

'''
 Create a new file named my_functions.py. Move your function from exercise1 to this file. Name this function "ssh_command". Reuse functions from this file for the rest of the exercises.
Move all of the device specific output printing to the called function (i.e. to the child thread).
'''

# import modules
from netmiko import ConnectHandler



def ssh_command(device, command):
    connection = ConnectHandler(**device)
    output = connection.send_command(command)
    connection.disconnect()
    print("=-" *30)
    print(("{} router command output:\n" + "=-" *30 +"\n" +  "{}").format(device["host"], output))
    print("=-" *30 + "\n\n")
    return


def ssh_command2(device, command):
    connection = ConnectHandler(**device)
    output = connection.send_command(command)
    connection.disconnect()
    return output



