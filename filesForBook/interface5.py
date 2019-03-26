#!/usr/bin/env python

def get_networks(gateways_dict):
	networks_dict = {}
	for key, value in gateways.iteritems():
		gateway_ip, iface = value[0], value[1]
		hwaddress, addr, broadcast, netmask = get_addresses(iface)
		network = {'gateway': gateway_ip, 'hwaddr' : hwaddress,
		'addr' : addr, 'broadcast' : broadcast, 'netmask' : netmask}
		networks_dict[iface] = network
	return networks_dict