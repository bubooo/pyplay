#!/usr/bin/env python3

''''
7a. Create an nxapi_plumbing "Device" object for nxos1. The api_format should be "xml" and the transport should be "https" (port 8443). Use getpass() to capture the device's password. Send the "show interface Ethernet1/1" command to the device, parse the output, and print out the following information:

Interface: Ethernet1/1; State: up; MTU: 1500



7b. Run the following two show commands on the nxos1 device using a single method and passing in a list of commands: "show system uptime" and "show system resources". Print the XML output from these two commands.


7c. Using the nxapi_plumbing config_list() method, configure two loopbacks on nxos1 including interface descriptions. Pick random loopback interface numbers between 100 and 199.

'''

# import modules
from nxapi_plumbing import Device
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning 
from getpass import getpass
from lxml import etree
import os

# Define variale intial value

router_password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()


# Define CONSTANTS

NXOS1 = {
    "api_format":"xml",
    "host":"nxos1.lasthop.io",
    "username":"pyclass",
    "password":router_password,
    "transport":"https",
    "port":"8443",
    "verify":False,
    }

SHOW_COMMANDS = [
    "show system uptime",
    "show system resources"]

CONFIG_LOOPBACK = [
    "interface loopback101",
    "ip address 11.11.11.1/24",
    "no shut",
    "interface loopback102",
    "ip address 12.12.12.2/24",
    "no shut"]

# Define variable initial values



#Define functions


# The CODE

if __name__ == "__main__":
    nxos1_conn = Device(**NXOS1)
    interface_show = nxos1_conn.show("show interface Ethernet1/1") 
    eth1_1 = interface_show.find(".//ROW_interface")
    print("+=" *30)
    # Nice exaple python's indentation feature and readability
    print("Interface: {}; State: {}; MTU: {}".format(
                                    interface_show.find(".//interface").text, 
                                    interface_show.find(".//state").text, 
                                    interface_show.find(".//eth_mtu").text)
        )
    print("+=" *30)

    # 7b
    show_commands_result = nxos1_conn.show_list(SHOW_COMMANDS)
    # print resut
    print("Result of show commands:")
    for command_result in show_commands_result:
        print(etree.tostring(command_result, encoding="unicode"))
    print("+=" *30)
    
    # 7c
    print("Configuring Loopback interfaces")
    result = nxos1_conn.config_list(CONFIG_LOOPBACK)
    # print XML output of each command
    for output_message in result:
        print(etree.tostring(output_message, encoding="unicode"))
'''
In [11]: pprint(etree.tostring(interface_show).decode())
('<output>\n'
 '      <body>\n'
 '        <TABLE_interface>\n'
 '         <ROW_interface>\n'
 '          <interface>Ethernet1/1</interface>\n'
 '          <state>up</state>\n'
 '          <admin_state>up</admin_state>\n'
 '          <share_state>Dedicated</share_state>\n'
 '          <eth_hw_desc>100/1000/10000 Ethernet</eth_hw_desc>\n'
 '          <eth_hw_addr>000c.29d1.0001</eth_hw_addr>\n'
 '          <eth_bia_addr>5254.0012.345e</eth_bia_addr>\n'
 '          <eth_mtu>1500</eth_mtu>\n'
 '          <eth_bw>1000000</eth_bw>\n'
 '          <eth_dly>10</eth_dly>\n'
 '          <eth_reliability>255</eth_reliability>\n'
 '          <eth_txload>1</eth_txload>\n'
 '          <eth_rxload>1</eth_rxload>\n'
 '          <encapsulation>ARPA</encapsulation>\n'
 '          <medium>broadcast</medium>\n'
 '          <eth_duplex>full</eth_duplex>\n'
 '          <eth_speed>1000 Mb/s</eth_speed>\n'
 '          <eth_beacon>off</eth_beacon>\n'
 '          <eth_autoneg>on</eth_autoneg>\n'
 '          <eth_in_flowctrl>off</eth_in_flowctrl>\n'
 '          <eth_out_flowctrl>off</eth_out_flowctrl>\n'
 '          <eth_mdix>off</eth_mdix>\n'
 ' '          <encapsulation>ARPA</encapsulation>\n'
 '          <medium>broadcast</medium>\n'
 '          <eth_duplex>full</eth_duplex>\n'
 '          <eth_speed>1000 Mb/s</eth_speed>\n'
 '          <eth_beacon>off</eth_beacon>\n'
 '          <eth_autoneg>on</eth_autoneg>\n'
 '          <eth_in_flowctrl>off</eth_in_flowctrl>\n'
 '          <eth_out_flowctrl>off</eth_out_flowctrl>\n'
 '          <eth_mdix>off</eth_mdix>\n'
 '          <eth_swt_monitor>off</eth_swt_monitor>\n'
 '          <eth_ethertype>0x8100</eth_ethertype>\n'
 '          <eth_eee_state>n/a</eth_eee_state>\n'
 '          <eth_link_flapped>5week(s) 2day(s)</eth_link_flapped>\n'
 '          <eth_clear_counters>never</eth_clear_counters>\n'
 '          <eth_reset_cntr>5</eth_reset_cntr>\n'
 '          <eth_load_interval1_rx>30</eth_load_interval1_rx>\n'
 '          <eth_inrate1_bits>0</eth_inrate1_bits>\n'
 '          <eth_inrate1_pkts>0</eth_inrate1_pkts>\n'
 '          <eth_load_interval1_tx>30</eth_load_interval1_tx>\n'
 '          <eth_outrate1_bits>0</eth_outrate1_bits>\n'
 '          <eth_outrate1_pkts>0</eth_outrate1_pkts>\n'
 '          <eth_inrate1_summary_bits>0 bps</eth_inrate1_summary_bits>\n'
'''

