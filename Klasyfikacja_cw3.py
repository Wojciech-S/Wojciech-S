class ElectricCar:
    pass

#car = ElectricCar(100) #ilość kilometrów, które przejedzie
#car.drive(70) #ile już przejechaliśmy
#charge #ładowanie baterii
def test_dystans_max(self):
    car = ElectricCar(100)
    assert car.dystans() == 100

def test_dystans_mozliwy(self):
    car = ElectricCar(100)
    car.drive(70)
    assert car.drive() == 70
    assert car.drive() == 100

def test_dystans_ponad(self):
    car = ElectricCar(100)
    car.drive(120)
    assert car.drive() == 100

def test_charge(self):
    car = ElectricCar(100)
    car.charge() == 100