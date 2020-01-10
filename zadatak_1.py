broj_alfonaca = 5000000
broj_velonaca = 9000000
broj_godina = 0

while broj_velonaca >= broj_alfonaca:
    broj_godina += 1
    broj_alfonaca = int(broj_alfonaca * 1.06)

    if broj_godina % 4 == 0:
        broj_velonaca = int(broj_velonaca * 1.05) - 500000

    else:
        broj_velonaca = int(broj_velonaca * 1.02)

print(f"Broj Alfonaca premašiti će broj Velonaca za {broj_godina} godina. Ukupan broj Alfonaca te godine = {broj_alfonaca}. ")
