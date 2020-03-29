import datetime
current_year = datetime.datetime.now()

wiek = int(input("W którym roku się urodziłeś? "))
if wiek <= 2002:
    print("Jesteś osobą pełnoletnią")
else:
    print("Jesteś niepełnoletni")
