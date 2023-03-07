#!/usr/bin/env python3

import NMtcpdump
import NMdhcp
import NMsnmp
import Mgithub

file = 'pcaps/objective2dot5.pcap'

mac_addr = 'ca02.0a55.0008'
#mac_addr = 'ca:02:0a:55:00:08'
#mac_addr = 'ca:03:0a:69:00:08'
arr = NMtcpdump.get_ips(file)
NMtcpdump.get_macs(arr)
NMdhcpserver.get_client_id(mac_addr)
NMsnmp.main_1()
