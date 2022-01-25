#!/usr/bin/env python3

import yaml



# Function to open yaml file

def read_yaml(file):
    with open(file) as f:
        return yaml.safe_load(f) 
    raise ValueError("Can't read YAML file")

def print_arp(structure):
    print("Device ARP table:")
    print("=-" *30)
    for device in structure:
        for entry in device["result"]["ipV4Neighbors"]:
            print(f'{entry["address"]}\t:\t{entry["hwAddress"]}')

