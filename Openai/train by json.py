import openai
from urllib.request import urlopen
from datetime import date
from bs4 import BeautifulSoup
import json

today = date.today().strftime("%Y/%m/%d")
html = urlopen(f"https://jeju-s.jje.hs.kr/jeju-s/food/{today}/lunch")
soup = BeautifulSoup(html, "html.parser")
lunch=soup.select("div:nth-child(2) > ul > li:nth-child(2) > dl > dd")

for m in lunch:
    menu=m.text.strip().split(" ")


openai.api_key = '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'

with open('ai.json', 'r', encoding='urf-8') as f:
    messages = json.load(f)


# messages.append({"role":"system", "content": ""})
# messages.append({"role":"user", "content": ""})
# messages.append({"role":"assistatnt", "content": ""})

while True:
    question=input("q : ")
    if question == "": break
    messages.append({"role":"user", "content": question})

    aiObj = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages
    )

    response=aiObj['choices'][0]['message']['content']
    # Ai가 답변한 내용

    print(f"AI : {response}")