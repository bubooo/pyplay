#!/usr/bin/env python3

'''
Namespaces in XML help to differentiate between conflicting element names. 

5a. Load the show_version.xml file (originally from a Cisco NX-OS device) using the etree.fromstring() method. Note this XML document, unlike the previous documents, contains the document encoding information. Because the document encoding is at the top of the file, you will need to read the file using "rb" mode (the "b" signifies binary mode). Print out the the namespace map of this XML object. You can accomplish this by using the .nsmap attribute of your XML object.


5b. Similar to earlier exercises, use the find() method to access the text of the "proc_board_id" element (serial number). As this XML object contains namespace data, you will need to use the {*} namespace wildcard in the find() method. Your find call should look as follows:

​find(".//{*}proc_board_id")


The {*} is a namespace wildcard and says to match ALL namespaces.
'''

# import modules
from lxml import etree
from pprint import pprint

# Define CONSTANTS
PATH = "./"
FILE = "show_version.xml"

# Define variable initial value

# Define functions

def read_xml(file):
    with open(file, "rb") as f_xml:
        return etree.fromstring(f_xml.read())

# THE CODE

if __name__ == "__main__":
    show_ver_xml = read_xml(PATH+FILE)
    print(20 * "=")
    # printing namespace
    print("Document namespace: \n{}".format(show_ver_xml.nsmap))
    #print("Default namespace: {}".format(show_ver_xml.nsmap[None]))
    print(20 * "=")

    # proc_board element text find using wildcard {*}
    print("Router serial number: {}".format(show_ver_xml.find(".//{*}proc_board_id").text))
