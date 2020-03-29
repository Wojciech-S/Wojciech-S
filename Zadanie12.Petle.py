dni = 7
temperat = 0
while dni > 0:
    temp = int(input("Temperatura dobowa: "))
    dni = dni -1
    temperat += temp

print(f"Średnia temperatura dobowa: {temperat/7}")