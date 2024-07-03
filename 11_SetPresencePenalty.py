"""
以presence_penalty參數控制重複機率
presence_penalty介於-2到2之間 越小重複機率越大
"""
import openai

openai.api_key = "OPENAI_API_KEY"

response1 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "用100字介紹獨角仙"}
    ],
    presence_penalty=-1.5,
)

response2 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "用100字介紹獨角仙"}
    ],
    presence_penalty=1.5,
)

print("-------------當presence_penalty值為-1.5時-------------")
print(response1.choices[0].message['content'].strip())

print("-------------當presence_penalty值為1.5時-------------")
print(response2.choices[0].message['content'].strip())