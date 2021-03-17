import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

url = "https://www.iban.com/currency-codes"
convert_url = "https://transferwise.com/gb/currency-converter/"


def extract_countries():
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    tds = soup.find_all("td")
    countries = []
    for index, td in enumerate(tds):
        if index % 4 == 2:
            country = {
                'name': tds[index-2].string.capitalize(), 'code': td.string}
            if tds[index-1].string != "No universal currency":
                countries.append(country)
    return countries


def print_countries(countries):
    for index, country in enumerate(countries):
        print(f"# {index} {country['name']}")


def convert(mycountry, another):
    print(
        f"\nHow many {mycountry} do you want to convert to {another}?")
    while(True):
        try:
            amount = float(input())
            result = requests.get(
                f"{convert_url}{mycountry}-to-{another}-rate?amount={amount}")
            soup = BeautifulSoup(result.text, "html.parser")
            rate = float(soup.find("span", {"class": "text-success"}).string)
            print(format_currency(amount, mycountry, locale="ko_KR"),
                  "is", format_currency(amount*rate, another, locale="ko_KR"))
            break

        except:
            print("That wasn't a number\n")
