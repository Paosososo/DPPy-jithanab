#!/usr/bin/env python3

first_num = int(input("Give me the first number: ").strip())
second_num = int(input("Give me the second number: ").strip())
print("Thank you!")

"""
print(f"{first_num} + {second_num} = {first_num + second_num}")
print(f"{first_num} - {second_num} = {first_num - second_num}")
print(f"{first_num} / {second_num} = {first_num // second_num}")
print(f"{first_num} * {second_num} = {first_num * second_num}")
"""

for op in ['+','-','/','*']:
    res = first_num//second_num if op == '/' else eval(f"{first_num} {op} {second_num}")
    #Ternary Conditional: "Set res equal to first_num // second_num IF op is equal to '/', ELSE set it equal to eval(...)."
    print(f"{first_num} {op} {second_num} = {res}")