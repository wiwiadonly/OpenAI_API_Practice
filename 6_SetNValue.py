"""
以n參數來設定回覆數量
n=1回覆一則 n=2回覆兩則 類推
"""

import openai

openai.api_key = "OPENAI_API_KEY"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "列舉3個好吃的台灣夜市小吃"}
    ],
    n=2
)

print(response)
print("回覆1")
print(response.choices[0].message['content'].strip())
print("---------------------------")
print("回覆2")
print(response.choices[1].message['content'].strip())