import openai
openai.api_key='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'

messages = []
messages.append({"role":"user", "content": "너의 이름은 춘식이고 제주과학고 1학년이야"})

while True:
    question=input("q: ")
    if question == "": break
    messages.append({"role":"user", "content": question})

    aiObj = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages
    )

    response=aiObj['choices'][0]['message']['content']
    # Ai가 답변한 내용

    print(f"AI : {response}")