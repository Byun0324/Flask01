import openai
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import date

today = date.today().strftime("%Y/%m/%d")
html = urlopen(f"https://jeju-s.jje.hs.kr/jeju-s/food/{today}/lunch")
soup = BeautifulSoup(html, "html.parser")
lunch = soup.select(".ulType_food > li:nth-child(2) > dl > dd")[0].text

openai.api_key = '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'

# {"role": "system", "content": "You are a helpful assistant."},
# {"role": "user", "content": "Who won the world series in 2020?"},
# {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
# {"role": "user", "content": "Where was it played?"}

messages = []
messages.append({"role": "system", "content": "너는 제주과학고등학교 학생이다."})
messages.append({"role": "system", "content": "너의 이름은 제돌이다."})
messages.append({"role": "system", "content": f"오늘의 점심은 {lunch}이다."})
messages.append({"role": "system", "content": "너의 나이는 16살이야"})


while True:
    question = input("me: ")
    if  question =="": break
   
    messages.append({"role": "user", "content": question})
   

    aiObj = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= messages
    )
    response=aiObj['choices'][0]['message']['content']
    print(f"AI: {response}")