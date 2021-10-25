#!/usr/bin/env python3

'''
4a. Use the find() method to retrieve the first "zones-security" element. Print out the tag of this element and of all its children elements. Your output should be similar to the following:

Find tag of the first zones-security element
--------------------
zones-security

Find tag of all child elements of the first zones-security element
--------------------
zones-security-zonename
zones-security-send-reset
zones-security-policy-configurable
zones-security-interfaces-bound
zones-security-interfaces


4b. Use the find() method to find the first "zones-security-zonename". Print out the zone name for that element (the "text" of that element).


4c. Use the findall() method to find all occurrences of "zones-security". For each of these security zones, print out the security zone name ("zones-security-zonename", the text of that element).

'''

# Import modules 
from lxml import etree

# Define CONSTANTS
PATH = ""
FILE = "show_security_zones.xml"

# Define variable initial value


# Define funtions



# THe CODE
# 4a
sec_zone_etree = etree.parse(PATH+FILE)
sec_zone_etree.getroot()
first_sec_zone = sec_zone_etree.find("zones-security")   # "./zones-security" is alternative also for first element

print("Find tag of first zones-security element")
print("-"*20)
print(first_sec_zone.tag)
print()

print("Find tag of all child elements of the first zones-security element")
print("-"*20)
for child in first_sec_zone:       # alternative is .getchildren() to get list of them as if single child element it wouldn't work
    print(child.tag)
print()
#4b
print("First Security zone name: {}".format(first_sec_zone.find("zones-security-zonename").text))
print("-"*20)
print()
# 4c
print("All Security zone names:")
print("-"*20)
all_sec_zone = sec_zone_etree.findall("zones-security")   # alternative to use".//zones-security" to tell explicitly to seach in all layers
for zone in all_sec_zone:
    print("Security zone name: {}".format(zone.find("zones-security-zonename").text))  # also can be use "./zones-security-zonename" to search in next layer only
print("\n\n")
