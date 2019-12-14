number = int(input("Enter row number: "))
n = 1
for x in range(1, number+1):
    for y in range(1, x+1):
        print(n, end="")
        n += 1
    print()