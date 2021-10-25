#!/usr/bin/env python3

'''
3a. Open the following two XML files: show_security_zones.xml and show_security_zones_single_trust.xml. Use a generic function that accepts an argument "filename" to open and read a file. Inside this function, use xmltodict to parse the contents of the file. Your function should return the xmltodict data structure. Using this function, create two variables to store the xmltodict data structure from the two files.


3b. Compare the Python "type" of the elements at ['zones-information']['zones-security']. What is the difference between the two data types? Why?


3c. Optional - create a second function that uses xmltodict to read and parse a filename that you pass in. This function should support a "force_list" argument that is passed to xmltodict.parse(). Reminder, the force_list argument of xmltodict takes a dictionary where the dictionary key-name is the XML element that is required to be a list. For example:

force_list={"zones-security": True}

Use this new function to parse the "show_security_zones_single_trust.xml". Verify the Python data type is now a list for the ['zones-information']['zones-security'] element.
'''

# import libraries
import xmltodict
from pprint import pprint


# Define CONSTANTS

PATH = ""
FILE1 = "show_security_zones.xml"
FILE2 = "show_security_zones_single_trust.xml"

# Define variable initial value


# Define functions

def parse_xml_file(file):
    
    with open(file) as xml_f:
        xml_string = xml_f.read()

    xml_dict = xmltodict.parse(xml_string)
    return(xml_dict)

# 3c Function with forced zones-security as list
def parse_xml_file_zone_list(file):
    
    with open(file) as xml_f:
        xml_string = xml_f.read()

    xml_dict = xmltodict.parse(xml_string, force_list = {"zones-security":True})
    return(xml_dict)

# THE CODE
# 3a
file1_xml = parse_xml_file(PATH+FILE1)
file2_xml = parse_xml_file(PATH+FILE2)

#3b

print("*"*10+" 3b "+"*"*10)
print("Type of {} file: {}".format(FILE1, type(file1_xml['zones-information']['zones-security'])))
print("Type of {} file: {}".format(FILE2, type(file2_xml['zones-information']['zones-security'])))

# 3c
print("*"*10+" 3c "+"*"*10)
print("Type of {} file with forced \"zone-security\" tag: {}".format(FILE2, type(parse_xml_file_zone_list(PATH+FILE2)['zones-information']['zones-security'])))
