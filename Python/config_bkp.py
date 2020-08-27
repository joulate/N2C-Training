#! /usr/bin/env python

#################################################################
### This scripts takes a device from user input, saves config ###
### and stores a copy on a directory.                         ###
###                                                           ###
###  V.1 - Jose Ulate                                         ###
###                                                           ###
#################################################################

from netmiko import ConnectHandler

def connect(device):
    print('\nConnecting to {}'.format(device))
    net_device = ConnectHandler(host=device, username='ntc', password='ntc123', device_type='cisco_ios')
    return net_device

def write_config(device, hostname):
    print('\nSaving config on device {}'.format(hostname))
    wr_mem = net_device.send_command('wr mem')
    print(wr_mem)


device = input('Enter device name:\n')
net_device = connect(device)
write_config(net_device, device)
