#Ogród doświadczalny
#Tworzymy postać ogrodnika, który porusza się po kwadratowej planszy symulującej ogród.
#W ogrodzie znajdują się trujace rośliny oraz narzędzia ogrodnicze.

import random

class Ogrodnik:
    def __init__(self, imie, wiedza, odpornosc, zdrowie=10):
        self.imie = imie
        self.wiedza = wiedza
        self.odpornosc = odpornosc
        self.zdrowie = zdrowie

    def start(self, x, y):
        self.x = x
        self.y = y
        self.x = random.randint(1, 10)
        self.y = random.randint(1, 10)

    def __str__(self):
        return f"Na imię mam: {self.imie}. Mój pozion wiedzy to {self.wiedza}, odporność: {self.odpornosc}, a zdrowie: {self.zdrowie}"

class TestOgrodnik:
    def test_init(self):
        gracz = Ogrodnik("Eryk", wiedza=8, odpornosc=7, zdrowie=10)
        assert gracz.imie == "Eryk"
        assert gracz.wiedza == 8
        assert gracz.odpornosc == 7
        assert gracz.zdrowie == 10

class PrzedmiotWiedza(Ogrodnik):
    def __init__(self, przedmiot, bonus_wiedza):
        self.przedmiot = przedmiot
        self.bonus_wiedza = bonus_wiedza

    def start(self, x, y):
        self.x = x
        self.y = y
        super().start(x, y)
        self.x = random.randint(1, 10)
        self.y = random.randint(1, 10)

    def __str__(self):
        return f"{self.przedmiot}: +{self.bonus_wiedza} do wiedzy"

class TestPrzedmiot_wiedza():
    def test_init(self):
        ekw1 = PrzedmiotWiedza("Konewka", 2)
        ekw2 = PrzedmiotWiedza("Encyklopedia roślin", 4)
        assert ekw1.przedmiot == "Konewka"
        assert ekw1.bonus_wiedza == 2
        assert ekw2.przedmiot == "Encyklopedia roślin"
        assert ekw2.bonus_wiedza == 4

class PrzedmiotOdp(Ogrodnik):
    def __init__(self, przedmiot, bonus_odp):
        self.przedmiot = przedmiot
        self.bonus_odp = bonus_odp

    def start(self, x, y):
        self.x = x
        self.y = y
        super().start(x, y)
        self.x = random.randint(1, 10)
        self.y = random.randint(1, 10)

    def __str__(self):
        return f"{self.przedmiot}: +{self.bonus_odp} do odporności"

class TestPrzedmiot_odp():
    def test_init(self):
        ekw3 = PrzedmiotOdp("Rękawice", 2)
        ekw4 = PrzedmiotOdp("Przyłbica", 4)
        assert ekw3.przedmiot == "Rękawice"
        assert ekw3.bonus_odp == 2
        assert ekw4.przedmiot == "Przyłbica"
        assert ekw4.bonus_odp == 4

class PrzedmiotZdrowie(Ogrodnik):
    def __init__(self, przedmiot, bonus_zdrowie):
        self.przedmiot = przedmiot
        self.bonus_zdrowie = bonus_zdrowie

    def start(self, x, y):
        self.x = x
        self.y = y
        super().start(x, y)
        self.x = random.randint(1, 10)
        self.y = random.randint(1, 10)

    def __str__(self):
        return f"{self.przedmiot}: może przywrócić utracone zdrowie o +{self.bonus_zdrowie}"

class TestPrzedmiot_zdrowie():
    def test_init(self):
        ekw1 = PrzedmiotZdrowie("Maść", 2)
        ekw2 = PrzedmiotZdrowie("Serum", 3)
        assert ekw1.przedmiot == "Maść"
        assert ekw1.bonus_zdrowie == 2
        assert ekw2.przedmiot == "Serum"
        assert ekw2.bonus_zdrowie == 3

class Rosliny(Ogrodnik):
    def __init__(self, nazwa, jad, odpornosc, zdrowie):
        self.nazwa = nazwa
        self.jad = jad
        self.odpornosc = odpornosc
        self.zdrowie = zdrowie

    def start(self, x, y):
        self.x = x
        self.y = y
        super().start(x, y)
        self.x = random.randint(1, 10)
        self.y = random.randint(1, 10)

    def __str__(self):
        return f"{self.nazwa}: poziom jadu: {self.jad}, odporność: {self.odpornosc}, wytrzymałość: {self.zdrowie}"

class Polozenie:
    def __init__(self, x, y, zasieg_x=10, zasieg_y=10):
        self.x = x
        self.y = y
        self.zasieg_x = zasieg_x
        self.zasieg_y = zasieg_y

    def g(self, n=1):
        self.y += n
        if self.y >self.zasieg_y:
            raise ValueError("Usiłujesz wyjść poza ogród.")

    def d(self, n=1):
        self.y -= n
        if self.y < self.zasieg_y:
            raise ValueError("Usiłujesz wyjść poza ogród.")

    def p(self, n=1):
        self.x += n
        if self.x > self.zasieg_x:
            raise ValueError("Usiłujesz wyjść poza ogród.")

    def l(self, n=1):
        self.x -= n
        if self.x > self.zasieg_x:
            raise ValueError("Usiłujesz wyjść poza ogród.")

    def __str__(self):
        return f"Twoja pozycja w ogrodzie to: x={self.x}, y={self.y}"

class TestPolozenie():
    def test_init(self):
        postac = Polozenie(2, 10)
        assert postac.x == 2
        assert postac.y == 10

class Ekwipunek: #Zbieranie przedmiotów
    pass

class Walka(Ogrodnik, Rosliny):
    pass

gracz = input("Wybierz imię dla Ogrodnika: ")
wiedza_pocz = int(input("Poziom wiedzy i odporności łącznie wynosi: 15. Jaki chcesz mieć początkowy poziom wiedzy [5-10]?: "))
odpornosc_pocz = (15 - wiedza_pocz)
if wiedza_pocz >= 5 and wiedza_pocz <= 10:
    print(f"Poziom wiedzy: {wiedza_pocz}, poziom odporności: {odpornosc_pocz}")
else:
    print("Poziom wiedzy może być jedynie w zakresie 5-10.")

ogrodnik = Ogrodnik(gracz, wiedza_pocz, odpornosc_pocz)
ogrodnik.__init__(gracz, wiedza_pocz, odpornosc_pocz)
x = random.randint(1, 10)
y = random.randint(1, 10)
start = Polozenie(x, y)