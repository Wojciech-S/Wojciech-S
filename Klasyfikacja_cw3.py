class ElectricCar(100):
    pass

#car = ElectricCar(100) #ilość kilometrów, które przejedzie
#car.drive(70) #ile już przejechaliśmy
#charge #ładowanie baterii
car = ElectricCar(100)
car.drive(70)
car.charge = car

def test_dystans_max():
    car = ElectricCar(100)
    assert car.dystans_max == 100

def test_dystans_mozliwy():
    car = ElectricCar(100)
    car.drive(70)
    assert car.dystans_mozliwy(70) == 70
    assert car.dystans_mozliwy(100) == 100

def test_dystans_ponad():
    car = ElectricCar(100)
    car.drive(120)
    assert car.dystans_ponad(120) == 100

def test_charge():
    car = ElectricCar(100)
    car.charge == car.dystans
    assert car.charge == 100