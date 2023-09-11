import openai
from urllib.request import urlopen
from datetime import date
from bs4 import BeautifulSoup

today = date.today().strftime("%Y/%m/%d")
html = urlopen(f"https://jeju-s.jje.hs.kr/jeju-s/food/{today}/lunch")
soup = BeautifulSoup(html, "html.parser")
lunch=soup.select("div:nth-child(2) > ul > li:nth-child(2) > dl > dd")

for m in lunch:
    menu=m.text.strip().split(" ")


openai.api_key = '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'

messages = []
messages.append({"role":"system", "content": "너는 제주과학고 1학년이야"})
messages.append({"role":"system", "content": "네 이름은 재돌이야"})
messages.append({"role":"system", "content": f"오늘 점심 메뉴는 {menu}이야"})


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