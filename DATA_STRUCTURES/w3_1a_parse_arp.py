#!/usr/bin/env python3

'''
Using the below ARP data, create a five element list. Each list element should be a dictionary with the following keys: "mac_addr", "ip_addr", "interface". At the end of this process, you should have five dictionaries contained inside a single list.

Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
'''
# Import modules
from pprint import pprint
import re

# define variable initial value
show_arp = '''
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
'''
#entry_dict = {}
new_list = []

# Define functions


if __name__ == "__main__":
    show_arp = show_arp.strip()
    arp_lines = show_arp.splitlines()
    for string in arp_lines:
        if re.search(r'^Protocol.*',string):
            continue
        _, ip_add, _, mac_add, _, interface = string.split()
        entry_dict = {"mac_addr":mac_add, "ip_addr": ip_add, "interface": interface}
        new_list.append(entry_dict)
    print("+" *20)
    pprint(new_list)        

