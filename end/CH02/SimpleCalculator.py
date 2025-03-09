#!/user/bin/env python3
# A simple calculator script in python
# Created by Quentin Athula, 3/9/2025

# Get input from the user
# Note we are casting the numbers as "float", we could also cast them as "int"
first_num = float(input("What is the first number: "))
activity = input("What activity? ( + - * / ) ")
second_num = float(input("What is the second number: "))

# depending on the selected activity, perform the calculation
if activity == "+":
    print(first_num + second_num)
if activity == "-":
    print(first_num - second_num)
if activity == "*":
    print(first_num * second_num)
if activity == "/":
    print(first_num / second_num)

