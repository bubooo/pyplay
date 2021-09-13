#!/usr/bin/env python3

'''
Using your TextFSM template and the 'show interface status' data from exercise2, create a Python program that uses TextFSM to parse this data. In this Python program, read the show interface status data from a file and process it using the TextFSM template. From this parsed-output, create a list of dictionaries. The program output should look as follows:

$ python ex7_show_int_status.py 

[{'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/0',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/1',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/2',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/3',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'}]
'''
# Import modules
import textfsm
from pprint import pprint


# Define variable initial value
dict_data = []

# Define CONSTANTs
PATH = "/home/bucko/pyplay/TEXTFSM/"
TEMPLATE_FILE = "w4_2_show_interface_status_more_columns.tpl"
INPUT_DATA_FILE = "fsm_show_interface_status.out"

# Define functions


# CODE
with open(PATH+TEMPLATE_FILE) as f_template:
    template = textfsm.TextFSM(f_template)

with open(PATH+INPUT_DATA_FILE) as f_data:
    input_data =f_data.read()

parsed_data = template.ParseText(input_data)
dict_keys = template.header
for list in parsed_data:
    dict_data.append(dict(zip(dict_keys,list))) 

print("a")
pprint(dict_data)
print("b")
