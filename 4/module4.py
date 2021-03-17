import requests
from bs4 import BeautifulSoup


def extract_brands():
    result = requests.get("http://www.alba.co.kr")
    soup = BeautifulSoup(result.text, "html.parser")
    superbrand = soup.find("div", {"id": "MainSuperBrand"})

    names = superbrand.find_all("strong")
    sites = superbrand.find_all("a", {"class": "brandHover"} or {
                                "class": "brandHover multi second"} or {"class": "brandHover multi"})
    brands = []
    for index in range(len(names)):
        brand = {'name': names[index].text, 'site': sites[index]['href']}
        brands.append(brand)
    return brands


def extract_onebrand(pages, url):
    jobs = []
    for index in range(pages):
        result = requests.get(f"{url}?page={index+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        normalinfo = soup.find("div", {"id": "NormalInfo"})
        rows = normalinfo.find_all("tr", {"class": ""})
        for row in rows:
            print(row)
            location = row.find("td", {"class": "local first"})
            print(location)
            # if location:
            #     location.replace("&nbsp", " ")
            company = row.find("span", {"class": "company"})
            print(company)
            time = row.find("td", {"class": "data"} or {
                            "class": "consult"})
            print(time)
            pay = row.find("td", {"class": "pay"})
            print(pay)
            date = row.find("td", {"class": "regDate last"})
            print(date)
            job = {'location': location,
                   'company': company,
                   'time': time,
                   'pay': pay,
                   'date': date}

            jobs.append(job)
            print(job)
    # print(jobs)
    return jobs
