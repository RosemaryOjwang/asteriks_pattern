rows = int(input("Enter an number: "))
#defining rows
for i in range(0, rows):
    for j in range(0, i+1):
        print("*", end="")
    print("\r")
for k in range(rows, 0, -1):
    for l in range(0, k-1):
        print("*", end="")
    print("\r")
