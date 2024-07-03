"""
使用top_p參數控制回覆內容
top_p介於0-1之間 越小出現一樣的機率越大
"""

import openai

openai.api_key = "OPENAI_API_KEY"

response1 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "用20字介紹台北科大"}
    ],
    top_p=0.15,
    n=2
)

response2 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "用20字介紹台北科大"}
    ],
    top_p=0.85,
    n=2
)

print("-------------當top_p值為0.15時-------------")
print("回覆1")
print(response1.choices[0].message['content'].strip())
print("---------------------------")
print("回覆2")
print(response1.choices[1].message['content'].strip())

print("-------------當top_p值為0.85時----")
print("回覆1")
print(response2.choices[0].message['content'].strip())
print("---------------------------")
print("回覆2")
print(response2.choices[1].message['content'].strip())