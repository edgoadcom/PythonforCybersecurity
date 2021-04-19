#!/usr/bin/env python3
# example workign with Loops
#By Ed Goad
# date: 2/5/2021

# Suggestion
# build out 1 function at a time and walk through them with the debugger
# not necessary to run all functions

def forLoop():
    for x in range(6):
        print(x)
def whileLoop():
    count = 0
    while (count < 6):
        print('The count is:', count)
        count = count + 1

def basicLoopElse():
    for x in range(6):
        print(x)
    else:
        print("Finally finished!")

def loopArray():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)
def loopArray2():
    for x in "banana":
     print(x)

def loopBreak():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)
        if x == "banana":
            break
def loopBreak2():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        if x == "banana":
            break
        print(x)
def loopContinue():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        if x == "banana":
            continue
        print(x)
def loopPass():
    for letter in 'Python': 
        if letter == 'h':
            pass
            print('This is pass block')
        print('Current Letter :', letter)
    print("Good bye!")

def nestedLoop():
    adj = ["red", "big", "tasty"]
    fruits = ["apple", "banana", "cherry"]
    for x in adj:
        for y in fruits:
            print(x, y)

#forLoop()
#whileLoop()
#basicLoopElse()
#loopArray()
#loopArray2()
#loopBreak()
#loopBreak2()
#loopContinue()
#loopPass()
#nestedLoop()