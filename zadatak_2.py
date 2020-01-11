krvna_grupa_primatelja = input("Krvna grupa primatelja: ").lower()
rh_faktor_primatelja = input("Rh faktor primatelja: ").lower()
krvna_grupa_donora = input("Krvna grupa donora: ").lower()
rh_faktor_donora = input("Rh faktor donora: ").lower()

                                     # ako nešto djeluje suvišno ne znači da je tako :)
if (rh_faktor_primatelja == "+" and (rh_faktor_donora == "-" or rh_faktor_donora == "+"))\
or (rh_faktor_primatelja == "-" and rh_faktor_primatelja == rh_faktor_donora):

    if krvna_grupa_donora == "0":
        print("Dozvoljena transfuzija")
    elif krvna_grupa_primatelja == krvna_grupa_donora:
        print("Dozvoljena transfuzija")
    elif krvna_grupa_primatelja == "ab":
        print("Dozvoljena transfuzija")
    else:
        print("Nedozvoljena transfuzija")

else:
    print("Nedozvoljena transfuzija")

