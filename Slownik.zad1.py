produkty = {
    "kiełbasa": 23,
    "szynka": 35,
    "baleron": 22,
    "pasztet": 18
}
magazyn = {
    "kiełbasa": 20,
    "szynka": 20,
    "baleron": 20,
    "pasztet": 20
}
print("Nasz sklepik oferuje: ")
for nazwa, cena in produkty.items():
    print(f" - {nazwa} w cenie: {cena} zł/kg ")
while True:
    tak = input("Czy zamieżasz coś kupić? [t-tak] [n-nie] [m-zobacz, czy towar jest w magazynie]")
    if tak == "n":
        break
    elif tak == "t":
        zakupy = input("Co chciałbyś kupić? ")
        if zakupy in produkty:
            miara = input(f"Jaką ilość produktu {zakupy} potrzebujesz? ")
            miara = float(miara)
            if miara <= magazyn[zakupy]:
                print(f"Za {miara} kg produktu {zakupy} cena wynosi {miara * produkty[zakupy]:.2f}")
                magazyn[zakupy] = magazyn[zakupy] - miara
            else: print("Nie mamy takiej ilości na stanie.")
    elif tak == "m":
        for nazwa, ilosc in magazyn.items():
            print(f" - {nazwa} w ilości: {ilosc} kg ")
        nowy = input("Jaki nowy towar dodajemy? ")
        cena2 = float(input("Jaka jest cena za kilogram? "))
        ilosc = float(input("Jaką ilość mamy? "))
        produkty[nowy] = cena2
        magazyn[nowy] = ilosc

        print("Nasz sklepik oferuje: ")
        for nazwa, cena in produkty.items():
            print(f" - {nazwa} w cenie: {cena} zł/kg ")
        print("Stan obecny w magazynie wynosi: ")
        for nazwa, ilosc in magazyn.items():
            print(f" - {nazwa} w ilości: {ilosc} kg ")
    else:
        print("Wpisz 't', 'n' lub 'm'.")

