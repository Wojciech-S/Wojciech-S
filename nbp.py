import sys
import requests
from collections import namedtuple

Waluta = namedtuple("currency", ["USD", "GBP", "EUR"])

if len(sys.argv) > 1:
    table = sys.argv[1]
else:
    table = "C"

def get_table(table):
    resp = requests.get(f"http://api.nbp.pl/api/exchangerates/tables/{table}/today/")
    rate = resp.json()[0]['rate']
    return rate

def get_currency(table):
    resp = requests.get("https://api.nbp.pl/api/exchangerates/tables/C/?format=json")
    w = resp.json()['Rate'][1]
    waluta = Waluta(w['USD'], w['GBP'], w['EUR'])
    return waluta

def report(w, table):
    rep = f"Bieżący kurs sprzedaży walut\n"
    rep += f"Dolar amerykański: {w.USD:.4f zł}\n"
    rep += f"Funt szterling: {w.GBP:.4f zł}\n"
    rep += f"Euro: {w.EUR:.4f} zł\n"
    return rep

if __name__ == "__main__":
    table = get_table(table)
    waluta = get_currency(table)
    rep = report(waluta, table)
    print(rep)