#!/usr/bin/env python

import argparse
from subnetting import subnetting

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    subnet = subparsers.add_parser("subnet")
    subnet.add_argument("cidr", help="IPv4 network address in CIDR or network/subnet-mask format")

    args = parser.parse_args()
    if args.command == "subnet":
        subnetting(args.cidr)
