#!/usr/bin/env python3
from scapy.all import *
import ipaddress

file = 'pcaps/objective2dot5.pcap'
# citation
# https://stackoverflow.com/questions/37140846/how-to-convert-ipv6-link-local-address-to-mac-address-in-python
def ip_conv(ipv6):

    v6_split = ipv6.split(":")
    mac_arr = []
    for slice in v6_split[-4:]:

        len_slice = len(slice)

        while len_slice < 4:

            ## adding zeros
            slice = '0' + slice

        mac_arr.append(slice[:2])
        mac_arr.append(slice[-2:])

    # modify parts to match MAC value
    mac_arr[0] = "%02x" % (int(mac_arr[0], 16) ^ 2)

    del mac_arr[4]
    del mac_arr[3]

    mac_address_final = ":".join(mac_arr)
    print(mac_address_final)
    return(mac_address_final)


def get_ips(file):
    pcap = rdpcap(file)
    counter = 1
    v6_arr = []
    while counter < len(pcap):
        pkt = pcap[counter]
        # filter ICMPv6 request packets
        if pkt.haslayer(IPv6) and ICMPv6EchoRequest(pkt):
            # decompress v6 address and ensure lowercase
            v6_addr = ipaddress.IPv6Address(pkt['IPv6'].src)
            v6_addr = v6_addr.exploded.lower()
            # ignore cloud vm ipv6 and any link-locals
            if not v6_addr.endswith('5f36') and not v6_addr.startswith('fe80'):
                # drop dupes
                if v6_addr not in v6_arr:
                   v6_arr.append(v6_addr)
        # increment
        counter += 1
    return(v6_arr)

def get_macs(v6_arr):
    arr = []
    # iterate through array
    for item in v6_arr:
        # send ip to function
        mac_str = ip_conv(item)
        arr.append(mac_str)

        # for cisco format
        #cisco_mac = mac_str.replace(':', "")
        #cisco_mac = ".".join(get_cisco_mac(cisco_mac, 4))

    return arr

#arr = get_ips(file)
#print(arr)
#get_macs(arr)
