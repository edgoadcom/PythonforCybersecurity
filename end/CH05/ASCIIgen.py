#!/usr/bin/env python3
# ASCII generator
# Uses chr() to create ASCII characters
# By Ed Goad
# 2/27/2021

for i in range(127):
    print("{0}\t'{1}'".format(i,chr(i)))
