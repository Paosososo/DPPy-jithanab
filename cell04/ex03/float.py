#!/usr/bin/env python3

user_input = input("Give me a number: ").strip()

try:
    num = float(user_input)
    if num.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except:
    pass

