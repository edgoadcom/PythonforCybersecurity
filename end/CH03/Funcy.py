#!/usr/bin/env python3
# example workign with Functions
#By Ed Goad
# date: 2/3/2021

# Suggestions - 
#  build out 1 function at a time, from top down
#  comment out calls to functions that arent needed to keep the output clean
#  When finished, uncomment all calls, then put a breakpoint at first call
#  Use debugging to show difference between step-over, step-into, step-out

# Basic function example
def func1():
    print("I am a function")

# Function that adds numbers
def addNums(val1, val2):
    print(val1 + val2)

# Function that raises to exponent, default to squared
def power(number, exp=2):
    print(number ** exp)

# Fucntion that returns value
def cube(x):
    return x**3

func1()
addNums(2, 5)
power(5, 3)
power(5)
value = cube(5)
print("The answer is {0}".format(value))
power(value, 5)


print("The answer is {0}".format(cube(6)))