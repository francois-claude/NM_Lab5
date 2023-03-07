#!/usr/bin/env python3
import easysnmp
from easysnmp import Session
import subprocess
import os

def get_ipv6_1(ip):
    f = open("output1.txt", "w")
    cmd = ['snmpbulkwalk', '-v', '2c', '-c', 'public', ip, 'ipAddressIfIndex.ipv6']
    tmp = subprocess.run(cmd, stdout=f)
    f.close()
    with open("output1.txt", "r") as f:
        text = f.read().strip()
        f.close()
    text = text.split('\n')[1]
    text = text.split('"')[1][:-1]
    return(text)

def get_ipv6_2(ip):
    f = open("output2.txt", "w")
    cmd = ['snmpbulkwalk', '-v', '2c', '-c', 'public', ip, 'ipAddressIfIndex.ipv6']
    tmp = subprocess.run(cmd, stdout=f)
    f.close()
    with open("output2.txt", "r") as f:
        text = f.read().strip()
        f.close()
    text = text.split('\n')[0]
    text = text.split('"')[1][:-1]
    return(text)

def main_1():
    # r1
    session = Session(hostname='192.168.0.10', community='public', version=1)
    r1_name = session.get('ifName.3')
    r1_status = session.get('ifOperStatus.3')
    r1_ip_add_v4_1 = session.get('ipAdEntAddr.192.168.0.10')
    r1_ip_add_v6_1 = get_ipv6_2('192.168.0.10')

    print(r1_name.value)
    print(r1_status.value)
    print(r1_ip_add_v4_1.value)
    print(r1_ip_add_v6_1)

    # r2
    session = Session(hostname='10.0.0.20', community='public', version=1)
    r2_name = session.get('ifName.1')
    r2_status = session.get('ifOperStatus.1')
    r2_name_2 = session.get('ifName.3')
    r2_status_2 = session.get('ifOperStatus.3')
    r2_ip_add_v4_1 = session.get('ipAdEntAddr.10.0.0.20')
    r2_ip_add_v4_2 = session.get('ipAdEntAddr.192.168.0.7')
    r2_ip_add_v6_1 = get_ipv6_1('10.0.0.20')
    r2_ip_add_v6_2 = get_ipv6_2('10.0.0.20')

    print(r2_name.value)
    print(r2_status.value)
    print(r2_name_2.value)
    print(r2_status_2.value)
    print(r2_ip_add_v4_1.value)
    print(r2_ip_add_v4_2.value)
    print(r2_ip_add_v6_1)
    print(r2_ip_add_v6_2)

    # r3
    session = Session(hostname='10.0.0.30', community='public', version=1)
    r3_name = session.get('ifName.1')
    r3_status = session.get('ifOperStatus.1')
    r3_name_2 = session.get('ifName.3')
    r3_status_2 = session.get('ifOperStatus.3')
    r3_ip_add_v4_1 = session.get('ipAdEntAddr.10.0.0.30')
    r3_ip_add_v4_2 = session.get('ipAdEntAddr.192.168.0.8')
    r3_ip_add_v6_1 = get_ipv6_1('10.0.0.30')
    r3_ip_add_v6_2 = get_ipv6_2('10.0.0.30')

    print(r3_name.value)
    print(r3_status.value)
    print(r3_name_2.value)
    print(r3_status_2.value)
    print(r3_ip_add_v4_1.value)
    print(r3_ip_add_v4_2.value)
    print(r3_ip_add_v6_1)
    print(r3_ip_add_v6_2)

    # r4
    session = Session(hostname='198.51.100.4', community='public', version=1)
    r4_name = session.get('ifName.1')
    r4_status = session.get('ifOperStatus.1')
    r4_name_2 = session.get('ifName.3')
    r4_status_2 = session.get('ifOperStatus.3')
    r4_ip_add_v4_1 = session.get('ipAdEntAddr.10.0.0.7')
    r4_ip_add_v4_2 = session.get('ipAdEntAddr.198.51.100.4')
    r4_ip_add_v6_1 = get_ipv6_1('198.51.100.4')
    r4_ip_add_v6_2 = get_ipv6_2('198.51.100.4')

    print(r4_name.value)
    print(r4_status.value)
    print(r4_name_2.value)
    print(r4_status_2.value)
    print(r4_ip_add_v4_1.value)
    print(r4_ip_add_v4_2.value)
    print(r4_ip_add_v6_1)
    print(r4_ip_add_v6_2)


    # r5
    session = Session(hostname='10.0.0.50', community='public', version=1)
    r5_name = session.get('ifName.1')
    r5_status = session.get('ifOperStatus.1')
    r5_ip_add_v4_1 = session.get('ipAdEntAddr.10.0.0.50')
    r5_ip_add_v6_1 = get_ipv6_2('10.0.0.50')
    print(r5_name.value)
    print(r5_status.value)
    print(r5_ip_add_v4_1.value)
    print(r5_ip_add_v6_1)

