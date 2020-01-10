težina_prtljage = input("Unesi težinu prtljage u kg: ")
težina_prtljage = float(težina_prtljage.replace(",", "."))  # ispravlja programsku grešku kod korištenja zareza za decimalne brojeve


if težina_prtljage < 0 or težina_prtljage > 50:
    print("Nedopušten unos.")
elif težina_prtljage <= 15:
    print("Nema nadoplate.")
else:
    nadoplata = (težina_prtljage - 15) * 50
    nadoplata = round(nadoplata, 2)
    print(f"Iznos nadoplate: {nadoplata} kn.")
