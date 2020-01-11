x = 0
y = 0
print("U = up, D = down, L = left, R = right Q = quit")


while True:
    command = input("Enter command: ").lower()
    if command == "u":
        y = y + 1
    elif command == "d":
        y = y - 1
    elif command == "l":
        x = x - 1
    elif command == "r":
        x = x + 1
    elif command != "u" and command != "d" and command != "l" and command != "r" and command != "q":
        print("Incorrect command!")
    else:
        if command == "q":
            break
print(f"Final position = ({x} : {y})")

