import openai
from urllib.request import urlopen
from datetime import datetime

today = date.today().strftime("%Y/%m/%d")
html = urlopen(f"https://jeju-s.jje.hs.kr/jeju-s/food/{today}/lunch")
soup = BeautifulSoup(html, "html.parser")
lunchmenu=soup.select("body > form > div > div > ul > li:nth-child(2) > dl > dd")[0].text

openai.api_key = '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'

messages = []
messages.append({"role":"system", "content": "너는 제주과학고 1학년이야"})
messages.append({"role":"system", "content": "너의 이름은 춘식이야"})
messages.append({"role":"system", "content": lunchmenu})

messages.append({"role":"system", "content": "오늘 점심 메뉴는 매운갈비찜과 수제비국이야"})


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