#!/usr/bin/env python3

'''
2a. Using xmltodict, load the show_security_zones.xml file as a Python dictionary. Print out this new variable and its type. Note, the newly created object is an OrderedDict; not a traditional dictionary.


2b. Print the names and an index number of each security zone in the XML data from Exercise 2a. Your output should look similar to the following (tip, enumerate will probably help):

Security Zone #1: trust
Security Zone #2: untrust
Security Zone #3: junos-host

'''

# Import libraries
from pprint import pprint
import xmltodict


# define CONSTANTS
PATH = ""
FILE = "show_security_zones.xml"

# define variable initial value



# define function



# THE CODE
with open(PATH + FILE) as xml_f:
    raw_xml = xml_f.read()

xml_dict = xmltodict.parse(raw_xml)

print("File {} type: {}".format(FILE, type(xml_dict)))
print("File {} contains:\n".format(FILE))
pprint(xml_dict)

# 2b excercise
print("File {} contains following security zones:".format(FILE))
for zone_index, zone in enumerate(xml_dict["zones-information"]["zones-security"]):
    print("Security zone #{}: {}".format(zone_index +1 , zone["zones-security-zonename"]))


