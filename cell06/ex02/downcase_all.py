#!/usr/bin/env python3
import sys
def downcase_it(s):
    return s.lower()

if __name__ == "__main__":
    params = sys.argv[1:]
    if not params: #params =[] (emptylist) , len(params) == 0
        print("none")
    else:
        for param in params:
            print(downcase_it(param))


