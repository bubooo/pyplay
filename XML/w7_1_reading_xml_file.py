#!/usr/bin/env python3

'''
1a. Using the show_security_zones.xml file, read the file contents and parse the file using etree.fromstring(). Print out the newly created XML variable and also print out the variable's type. Your output should look similar to the following:

​<Element zones-information at 0x7f3271194b48>
<class 'lxml.etree._Element'>


1b. Using your XML variable from exercise 1a, print out the entire XML tree in a readable format (ensure that the output string is a unicode string).


1c. Print out the root element tag name (this tag should have a value of "zones-information"). Print the number of child elements of the root element (you can retrieve this using the len() function).


1d. Using both direct indices and the getchildren() method, obtain the first child element and print its tag name. 


1e. Create a variable named "trust_zone". Assign this variable to be the first "zones-security" element in the XML tree. Access this newly created variable and print out the text of the "zones-security-zonename" child.


1f. Iterate through all of the child elements of the "trust_zone" variable. Print out the tag name for each child element.
'''

#Import libraries
from lxml import etree


#Define CONSTANTS
PATH = "."
FILE = "show_security_zones.xml"

#Definevariable initial value


# Define function

def print_var_type(var):
    print("This is XML variable info about")
    print(var)
    print(type(var))
    print("*="*20)

def print_xml_tree(var):
    print("This is XML tree element structure")
    print(etree.tostring(var).decode())
    print("*="*20)

def xml_root_tag(var):
    print("XML root element tag:{}".format(var.tag))
    print("XML root has {} children elements".format(len(var.getchildren())))
    print("*="*20)

def get_first_child_element_tag(etree_var):
    first_child = etree_var.getchildren()[0]
    print("XML root first child is: {}".format(first_child.tag))
    print("This is children element directly accessed: {}".format(etree_var[0]))
    print("*="*20)

def get_child_element_text(etree_var, child):
    element = etree_var.findall(".//"+child)
    return(element.text)
    
# THE CODE

with open(PATH+"/"+FILE) as f_xml:
    xml_string = etree.fromstring(f_xml.read())

print_var_type(xml_string)
print_xml_tree(xml_string)
xml_root_tag(xml_string)
get_first_child_element_tag(xml_string)

#1e
trust_zone = xml_string[0]
trust_zone_value = trust_zone.find("zones-security-zonename").text
print("See text field of element {}: {}".format("zones-security-zonename",trust_zone_value))
print("*="*20)

#1f
print("1F: This is list of all tags of {}:".format(trust_zone_value))
for child in trust_zone.iterdescendants():
    print(child.tag)
print("*="*20)
