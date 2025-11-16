size = int(input("Enter the size of the pattern: "))

row = 0

while row < size:
    for i in range(size):
        print("*", end="")
    print()  # move to next line
    row += 1

