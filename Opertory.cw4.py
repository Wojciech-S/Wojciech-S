#sortowanie liczb w tablicy przy wykorzystaniu algorytmu "sortowanie przez wybieranie"
lista = [9,1,6,8,4,3,2,0]
rob = set()
for i in lista:
    print(min(lista))
    rob.add(i)
    print(rob)
lista = rob
lista2 = [0,1,2,3,4,6,8,9]

print(lista.issubset(lista2))