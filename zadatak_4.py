x = (input("Unesi težinu prtljage u kg: "))
x = float(x.replace(",", "."))
z = nadoplata = (x-15) * 50
z = round(z, 2)

if x < 0 or x > 50:
    print("Nedopušten unos.")
elif x <= 15:
    print("Nema nadoplate.")
else:
    print("Iznos nadoplate: {0} kn".format(z))
