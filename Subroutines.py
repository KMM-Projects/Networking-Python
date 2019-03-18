#!/usr/bin/python3
__author__ = 'Patrik'


def sub(x,y):
    # out of scope
    z = x - y
    print(z)

# using parameters
def add(x,y):
    # return value
    return x + y

print(add(13,5))
# no passing parameters
sub(13,5)
