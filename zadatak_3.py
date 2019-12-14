x = 0
y = 0
print("U = up, D = down, L = left, R = right Q = quit")
z = ""

while True:
    z = input("Enter command: ").lower()
    for z in z:    #  moguće je unositi više naredbi u jednom redu
        if z == "u":
            y = y+1
            print("Position = ({0} : {1})".format(x, y))
        elif z == "d":
            y = y-1
            print("Position = ({0} : {1})".format(x, y))
        elif z == "l":
            x = x-1
            print("Position = ({0} : {1})".format(x, y))
        elif z == "r":
            x = x+1
            print("Position = ({0} : {1})".format(x, y))
        elif z != "u" and z != "d" and z != "l" and z != "r" and z != "q":
            print("Incorrect command!")
    else:
        if z == "q":
            break
print("Final position = ({0} : {1})".format(x,y))
