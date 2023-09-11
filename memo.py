import openai
from urllib.request import urlopen
from datetime import date
from bs4 import BeautifulSoup

today = date.today().strftime("%Y/%m/%d")
html = urlopen(f"https://jeju-s.jje.hs.kr/jeju-s/food/{today}/lunch")
soup = BeautifulSoup(html, "html.parser")
lunchmenu=soup.select("div:nth-child(2) > ul > li:nth-child(2) > dl > dd")

for m in lunchmenu:
    menu=m.text.strip().split(" ")

print(menu)