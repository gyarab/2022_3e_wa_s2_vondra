import httpx
from pprint import pprint

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"
res = httpx.get(url)
rows = res.text.split("\n")

rows = rows[2:-1]

"""
result = amount / data["USD"]
data = {
    "EUR": 23.880,
    "USD": 21.971,
    ...
}
"""

data = {}

for r in rows:
    cols = r.split("|")
    curr = cols[-2]
    rate = cols[-1]
    rate = rate.replace(",", ".")
    mnozstvi = cols[-3]
    rate = float(rate)
    mnozstvi = float(mnozstvi)
    rate = rate/mnozstvi
    
    data[curr] = rate
pprint(data)


while(True):
    user_curr = input("Zadej cílovou měnu: ")
    if user_curr.upper() in data:
        break
    else:
        print("Měna neexistuje")

while(True):
    user_amount = input("Zadej částku v cílové měně: ")
    try:
        user_amount = user_amount.replace(",", ".")
        user_amount = float(user_amount)
        break
    except ValueError:
        print("Špatný formát čísla")

result = user_amount * data[user_curr.upper()]
result = round(result, 2)

print(f"Vysledna castka je  {result} CZK")
