#!/bin/python3

user_input = input("What you gotta say? : ").strip()

while True:
    if user_input == "STOP":
        break
    user_input = input("I got that! Anything else? : ").strip()
