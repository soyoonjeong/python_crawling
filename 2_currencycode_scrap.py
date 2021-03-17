import os
import requests
from bs4 import BeautifulSoup

os.system("cls")
url = "https://www.iban.com/currency-codes"

print("Hello! Please choose select a country by number:")

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
tds = soup.find_all("td")
names = []
codes = []
for index, td in enumerate(tds):
    if index % 4 == 0:
        names.append(td.string)
    elif index % 4 == 2:
        codes.append(td.string)

for index, name in enumerate(names):
    print(f"# {index} {name}")
while True:
    try:
        select = int(input("#: "))
        if select < 0 or select >= len(names):
            print("Choose a number from the list.")
        else:
            print(f"You chose a {names[select]}.")
            print(f"The currency code is {codes[select]}.")
            break
    except:
        print("That wasn't a number.")
