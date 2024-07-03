""" 
使用SYSTEM角色來提問 
將role設為system來客製回覆身分
"""

import openai

openai.api_key = "OPENAI_API_KEY"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "你是一個棒球數據專家"},
        {"role": "user", "content": "幫我分析Harper和大谷翔平拿到國聯MVP的可能性各為多少"}
    ]
)
print("-------------回傳值為-------------")
print(response)
print("-------------content為-------------")
print(response.choices[0].message['content'].strip())

