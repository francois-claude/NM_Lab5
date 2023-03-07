#!/usr/bin/env python3

from netmiko import ConnectHandler
import re
import subprocess

mac_addr = 'ca02.0a55.0008'
#mac_addr = 'ca:02:0a:55:00:08'
#mac_addr = 'ca:03:0a:69:00:08'

R4 = {
    "device_type": "cisco_ios",
    "host": "198.51.100.4",
    "username": "netman",
    "password": "password123",
}

def get_client_id(mac_addr):
    subprocess.check_output("echo " + mac_addr + " | sed 's/\.//g' | sed -E 's/(.{2})/\1\n/g' | xxd -r -p", shell=True)

def get_R5_ip():
    command = "show cdp entry R5 | include IPv6"
    #command = "show ip int br"
    with ConnectHandler(**R4) as net_connect:
        output = net_connect.send_command(command)
        # remove whitespace
        output = output.replace(' ', '')
        output = output.replace('IPv6address:', '')
        output = re.sub(r'\([^,]*$', '', output)
        return output

R5 = {
    "device_type": "cisco_ios",
    "host": get_R5_ip(),
    "username": "netman",
    "password": "password123",
}

def ssh_to_r5():
    with ConnectHandler(**R5) as net_connect:
        ## configure R5 DHCP

        #cmds  = ['interface fa0/0']
        #cmds += ['shutdown']
        #cmds += ['no ip dhcp pool dhcp-pool']
        #cmds += ['no ip dhcp excluded-address 10.0.0.10']
        #cmds += ['no ip dhcp excluded-address 10.0.0.20']
        #cmds += ['no ip dhcp excluded-address 10.0.0.30']
        #cmds += ['no ip dhcp excluded-address 10.0.0.40']
        #cmds += ['no ip dhcp excluded-address 10.0.0.50']
        #cmds += ['no ip dhcp pool static1']
        #cmds += ['no ip dhcp pool static2']
        #cmds += ['interface fa0/0']
        #cmds += ['no shutdown']

        cmds  = ['interface fa0/0']
        cmds += ['shutdown']
        cmds += ['ip dhcp pool dhcp-pool']
        cmds += ['network 10.0.0.0 255.255.255.0']
        cmds += ['default-router 10.0.0.5']
        cmds += ['lease 0 1 0']
        cmds += ['ip dhcp excluded-address 10.0.0.10']
        cmds += ['ip dhcp excluded-address 10.0.0.20']
        cmds += ['ip dhcp excluded-address 10.0.0.30']
        cmds += ['ip dhcp excluded-address 10.0.0.40']
        cmds += ['ip dhcp excluded-address 10.0.0.50']
        cmds += ['ip dhcp pool static1']
        cmds += ['host 10.0.0.20 255.255.255.0']
        cmds += ['client-identifier 0063.6973.636f.2d63.6130.322e.3061.3535.2e30.3030.382d.4661.302f.30']
        cmds += ['0063.6973.636f.2d63.6130.322e.3061.3535.2e30.3030.382d.4661.302f.30']
        cmds += ['ip dhcp pool static2']
        cmds += ['host 10.0.0.30 255.255.255.0']
        cmds += ['client-identifier 0063.6973.636f.2d63.6130.332e.3061.3639.2e30.3030.382d.4661.302f.30']
        cmds += ['interface fa0/0']
        cmds += ['no shutdown']

        #cmds += ['']
        output = net_connect.send_config_set(cmds)

        output = net_connect.send_command("show ip dhcp binding")
        ip_list = re.findall( r'[0-9]+(?:\.[0-9]+){3}', output )
        return ip_list

get_client_id(mac_addr)
