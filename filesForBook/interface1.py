#!/usr/bin/env python

def get_ip(inter):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip_addr = socket.inet_ntoa(fcnt1.ioctl(s.fileno(), 0x8915, struct.pack('256s', inter[:15]))[20:24])
    return ip_addr
