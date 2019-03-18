#!/usr/bin/python3
__author__ = 'Patrik'

import os
from subprocess import call

#use the OS interface to get access to system information
print(os.getcwd())
print(os.getuid())
print(os.getenv("PATH"))

# using system
os.system("ls -la")
# can use call
inp = input("Hit Enter")
call(["ls","-la"])
