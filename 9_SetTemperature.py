"""
用temperature參數控制回覆內容
值介於0到2之間
越沒創意但出錯率不高 靠近2則越天馬行空
"""

import openai

openai.api_key = "OPENAI_API_KEY"

response1 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "列舉五個好吃的台灣夜市小吃"}
    ],
    temperature=0.1,
    n=2
)

response2 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "列舉五個好吃的台灣夜市小吃"}
    ],
    temperature=1.0,
    n=2
)

print("-------------當temperature值為0.1時-------------")
print("回覆1")
print(response1.choices[0].message['content'].strip())
print("---------------------------")
print("回覆2")
print(response1.choices[1].message['content'].strip())

print("-------------當temperature值為1.0時-------------")
print("回覆1")
print(response2.choices[0].message['content'].strip())
print("---------------------------")
print("回覆2")
print(response2.choices[1].message['content'].strip())