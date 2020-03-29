a = int(input("Podaj wysokość opakowania"))
b = int(input("Podaj szerokość opakowania"))
c= int(input("Podaj głębokość opakowania"))
obj = a*b*c

print()
print(f"Objętość opakowania wynosi: {obj} cm3")
print(f"Objętość przekracza 1 L?: {obj > 1000}")