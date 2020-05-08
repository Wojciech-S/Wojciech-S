#Zaimplementuj funkcję, która sprawdzi czy podany napis jest palindromem (napis czytany tak samo od
#lewej, jak i od prawej).
#Podpowiedź: do odwrócenia napisu możemy wykorzystać mechanizm wycinania (ang. slicing).

def czy_palindron(napis):
    normal = napis[0:]
    wspak = napis[::-1]
    if normal == wspak:
        print(True)
    else:
        print(False)
    return napis

napis = input("Podaj dowolny wyraz: ")
czy_palindron(napis)

def test_czy_to_palindron():
    assert "aaa" == True
    assert "ada" == True
    assert "kajak" == True
    assert "ul" == False
    assert "kot" == False
    assert "parapet" == False