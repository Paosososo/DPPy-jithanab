#!/usr/bin/env python3

print("Enter the first number: ")
first = int(input().strip())

print("Enter the second number: ")
second = int(input().strip())

result = first * second

print(f"{first} * {second} = {result}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is both positive and negative.")