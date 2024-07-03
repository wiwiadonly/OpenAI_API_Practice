import openai

openai.api_key = "OPENAI_API_KEY"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "用300字介紹獨角仙"}
    ],
    presence_penalty=-1.5,
    stream=True
)

for chunk in response:
    print(chunk)