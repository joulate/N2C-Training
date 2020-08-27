#! /usr/bin/env python

from netmiko import ConnectHandler


def ez_cisco(hostname, username, password, show_command):
    platform = 'cisco_ios'
    device = ConnectHandler(ip=hostname, username=username, password=password, device_type=platform)
    
    output = device.send_command(show_command)
    device.disconnect()

    return output


devices = ['csr1', 'csr2', 'csr3']

for device in devices:
    print('Connecting to {}'.format(device))
    print("*" * 20)
    response = ez_cisco(device, 'ntc', 'ntc123', 'show ip int brief')
    print(response)
    print("*" * 20)
