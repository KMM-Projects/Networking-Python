#!/usr/bin/python3
__author__ = 'Patrik'

# How to parse arguments to the python script

import argparse

parser = argparse.ArgumentParser(description="This is our description")
parser.add_argument('-i', type=str, help="Thi is he help you get to describe the parameter", required=True)
parser.add_argument('-o',type=str, help="This is optional", required=False)

#cmdargs end up being disctionary/hash

cmdarg = parser.parse_args()

# access the parameter based on flag
ivar = cmdarg.i
print(ivar)

