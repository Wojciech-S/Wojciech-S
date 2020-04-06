x = int(input("Podaj swoją współrzędną x: "))
y = int(input("Podaj swoją współrzędną y: "))

if (x < 0 or x > 100 or y < 0 or y > 100):
    print("Gracz znajduje się poza polem planszy.")
elif (x > 10 and x < 90) and (y > 10 and y >= 90):
    print("Gracz znajduje się przy Górnej krawędzi.")
elif (x > 10 and x < 90) and (y < 10):
    print("Gracz znajduje się przy Dolnej krawędzi.")
elif (x <= 10 and y <= 10):
    print("Gracz znajduje się w Lewym dolnym rogu.")
elif (x >= 90 and y <= 10):
    print("Gracz znajduje się w Prawym dolnym rogu.")
elif (x <= 10 and y >= 90):
    print("Gracz znajduje się w Lewym górny rogu.")
elif (x <= 10 and y > 10 and y < 90):
    print("Gracz znajduje się przy Lewej krawędzi.")
elif (x >= 90 and y >= 90):
    print("Gracz znajduje się w Prawym górnym rogu.")
elif (x >= 90 and y > 10 and y < 90):
    print("Gracz znajduje się przy Prawej krawędzi.")
else:
    print("Gracz znajduje się w Centrum.")
