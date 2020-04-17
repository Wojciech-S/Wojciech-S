liczba = int(input("Podaj dowolną liczbę naturalną większą od 0: "))
bok = ("*" + (" ") * (liczba - 2) + "*")
wys = (liczba-2)
if liczba <= 0:
    print("Ta liczba nie jest większa od 0.")
elif liczba == 1:
    print("*")
elif liczba == 2:
    print("**\n**")
else:
    print("*" * liczba)
    print(bok)
    while wys > 1:
        wys -=1
        print(bok)
    print("*"*liczba)