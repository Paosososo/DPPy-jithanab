#!/usr/bin/env python3
import sys



if len(sys.argv) != 3:
    print("none")
    sys.exit()

try:
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    if start <= end:
        arr = list(range(start, end + 1))
    else:
        arr = list(range(start, end -1, -1))

    print(arr)

except ValueError:
    print("none")