#!/usr/bin/python3
__author__ = 'Patrik'

# input is a string unless in converted

x = int(input("Give me a number:"))
if (x < 1):
    print("Too little")
elif (x >= 1 and x <= 10):
    print("Just about right")
else:
    print("Too High")


