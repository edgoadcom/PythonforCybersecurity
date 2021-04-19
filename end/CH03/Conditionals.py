#!/usr/bin/env python3
# example workign with conditionals
#By Ed Goad
# date: 2/3/2021

# Suggestion - 
#   add in <, ==, > one at a time
#   make each of them if statements initially
#   Change x and y values to test the various paths
#   eventually simplfy with if, elif, else

def condTest():
    x, y = 100, 10

    # First condition test, x is less than y
    if x < y:
        print("X is less than y")
    # Another conditional test, x is equal to y
    elif x == y:
        print("X is equal to y")
    # Last conditional test, x is greater than y
    else:
        print("X is greater than y")

condTest()