a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
op = input("Podaj rodzaj operacji: ")

if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/" and b != 0:
    print(a/b)
elif op == "/" and b == 0:
    print("Działanie niemożliwe")
else:
    print("Nieprawidłowy znak operacji")