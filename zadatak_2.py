a = input("Krvna grupa primatelja: ").lower()
b = input("Rh faktor primatelja: ").lower()
c = input("Krvna grupa donora: ").lower()
d = input("Rh faktor donora: ").lower()

if a != "a" and a != "b" and a != "ab" and a != "0":
    print("greška u unosu")
elif c != "a" and c != "b" and c != "ab" and c != "0":
    print("greška u unosu")
elif b != "-" and b != "+":
    print("greška u unosu")
elif d != "-" and d != "+":
    print("greška u unosu")
elif b == "+" or b == "-" == d:
    if a == "0" == c:
        print("Dozvoljena transfuzija")
    elif a == "a" == c or c == "0":
        print("Dozvoljena transfuzija")
    elif a == "b" == c or c == "0":
        print("Dozvoljena transfuzija")
    elif a == "ab" != c:
        print("Dozvoljena transfuzija")
    else:
        print("Nedozvoljena transfuzija")
else:
    print("Nedozvoljena transfuzija")
