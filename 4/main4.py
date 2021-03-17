import os
import requests
from bs4 import BeautifulSoup
from module4 import *

os.system("cls")
brands = extract_brands()
for brand in brands:
    result = requests.get(brand['site'])
    soup = BeautifulSoup(result.text, "html.parser")
    normalinfo = soup.find("div", {"id": "NormalInfo"})
    pages = int(normalinfo.find("strong").string)//50+1
    print(brand['name'], normalinfo.find("strong").string)
    jobs = extract_onebrand(pages, brand['site'])
    print(len(jobs))
    break
# 브랜드하나에서 일자리 불러오는 거 부터
