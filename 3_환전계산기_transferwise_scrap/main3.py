import os
import requests
from bs4 import BeautifulSoup
from module import *
from babel.numbers import format_currency


os.system("cls")
url = "https://www.iban.com/currency-codes"

print("Welcome to CurrencyConvert PRO 2000")

countries = extract_countries()

print_countries(countries)

while True:
    try:
        print("\nWhere are you from? Choose a country by number.\n")
        mycountry = countries[int(input("#: "))]
        print(mycountry['name'])
    except:
        print("That wasn't a number.")

while True:
    try:
        print("\nNow choose another country\n")
        another = countries[int(input("#: "))]
        print(another['name'])
    except:
        print("That wasn't a number.")


convert(mycountry['code'], another['code'])
