#!/usr/bin/env python3

import json

# Change MAC Addr
# ip link set dev <your device here> address <your new mac address>

# Change Ip Addr
# ip addr add 10.22.30.44/16 dev <your device here>

# Remove IP Addr
# ip addr flush dev <your device here>

# Set duplex mode
# ethtool -s [device_name] duplex [half/full]

# Set Speed
# ethtool -s [device_name] speed [10/100/1000]

# Set autoneg
# ethtool -s [device_name] autoneg [on/off]

def set_network_config(item:dict):
    if 'ifname' in item:
        ifname = item['ifname']
        print('ip link set dev {} down'.format(ifname))
        if 'addr' in item:
            print('ip addr flush dev {}'.format(ifname))
            print('ip addr add {} dev {}'.format(item['addr'], ifname))
        if 'mac' in item:
            print('ip link set dev {} address {}'.format(ifname, item['mac']))
        if 'speed' in item:
            print('ethtool -s {} speed {}'.format(ifname, item['speed']))
        if 'duplex' in item:
            print('ethtool -s {} duplex {}'.format(ifname, item['duplex']))
        if 'autoneg' in item:
            print('ethtool -s {} autoneg {}'.format(ifname, item['autoneg']))
        print('ip link set dev {} up'.format(ifname))
        
if __name__ == "__main__":
    config_file_path = 'configure.json'
    with open(config_file_path, 'r') as f:
        data = json.load(f)
        for item in data['network settings']:
            set_network_config(item)