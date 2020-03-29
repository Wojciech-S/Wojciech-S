#Wprowadzamy dowolną liczbę zmiennych, ustalonych samemu przez użytkownika.
#Należy podać wartość najwyższą i najniższą

min_a = None
max_a = None

while True:
    a = input("Podaj dowolną liczbę lub napisz x, jeśli chcesz zakończyć: ")
    if a == "x":
        break
    a = int(a)
    if min_a is None or a < min_a:
        min_a = a
    if max_a is None or a > max_a:
        max_a = a

print(f"Liczba maksymalna: {max_a}")
print(f"Liczba minimalna: {min_a}")
