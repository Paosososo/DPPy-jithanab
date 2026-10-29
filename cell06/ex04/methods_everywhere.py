#!/usr/bin/env python3
import sys

def shrink(s):
    print(s[:8])

def enlarge(s):
    paddings = 'Z' * (8 - len(s))
    print(s + paddings)

params = sys.argv[1:]
if not params:
    print("none")
else:
    for param in params:
        if len(param) > 8:
            shrink(param)
        elif len(param) < 8:
            enlarge(param)
        else:
            print(param)

