a = Broj_Alfonaca = 5000000
b = Broj_Velonaca = 9000000
n = broj_godina = 0

while b >= a:
    n += 1
    a = int(a * 1.06)
    if n % 4 == 0:
        b = int(b * 1.05) - 500000
    else:
        b = int(b * 1.02)

print("Broj Alfonaca premašit će broj Velonaca za {1} godina. Ukupan broj Velonaca te godine = {0}".format(a, n))