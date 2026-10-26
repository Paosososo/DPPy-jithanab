print("Enter a number less than 25")
num = int(input().strip())

if num > 25:
    print("Error")
else:
    while num <= 25:
        print(f"Inside the loop, my varaible is {num}")
        num += 1