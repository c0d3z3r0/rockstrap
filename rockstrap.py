#!/usr/bin/env python3

__author__ = "Michael Niewöhner"

import argparse
import sys
import os

# TODO: move argparse to armdebootstrap
def parseargs():
    parser = argparse.ArgumentParser(description='RPi2strap')
    parser.add_argument('sdcard', nargs=1,
                        help='SD card to install debian on e.g. /dev/sdc')
    parser.add_argument('--packages', "-p",
                        help='Comma separated list of additional packages')
    return parser.parse_args()


def main():

    args = parseargs()
    name = 'RockStrap'
    hostname = 'radxarock'
    sdcard = args.sdcard[0]
    partitions = [
        {'start': '', 'end': '', 'type': '83', 'fs': 'ext4',
         'mount': '/'}
    ]
    packages = []
    if args.packages:
        packages += args.packages.split(',')

    # Download latest armdebootstrap and create object
    os.system('curl -so armdebootstrap.py --connect-timeout 5 '
              'https://raw.githubusercontent.com/c0d3z3r0/armdebootstrap/'
              'master/armdebootstrap.py')
    from armdebootstrap import ArmDeboostrap
    adb = ArmDeboostrap(name, hostname, sdcard, partitions, packages)

    # Initialize ArmDebootstrap and start the installation process
    adb.init()
    adb.install()

    # ################### Radxa Rock specific stuff ####################

    #TODO: sd card booting stuff and kernel installation

    # ################### end Radxa Rock specific stuff ####################

    adb.cleanup()
    sys.exit(0)


if __name__ == '__main__':
    main()