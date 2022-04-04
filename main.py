#!/usr/bin/env python

import argparse
from subnetting import subnetting
from pingsweep import ping_sweep
from portscan import port_scan

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    subnet = subparsers.add_parser("subnet")
    subnet.add_argument("cidr", help="IPv4 network address in CIDR or network/subnet-mask format")

    ping = subparsers.add_parser("pingsweep")
    ping.add_argument("cidr", help="IPv4 network address in CIDR or network/subnet-mask format")

    scan = subparsers.add_parser("portscan")
    scan.add_argument("ip", help="Target IP address")
    scan.add_argument("first", help="The first port in range to be scanned", type=int)
    scan.add_argument("last", help="The last port in range to be scanned", type=int)

    args = parser.parse_args()
    if args.command == "subnet":
        subnetting(args.cidr)
    elif args.command == "pingsweep":
        ping_sweep(args.cidr)
    elif args.command == "portscan":
        port_scan(args.ip, args.first, args.last)
