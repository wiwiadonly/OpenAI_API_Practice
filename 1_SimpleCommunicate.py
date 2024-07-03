
"""# **第一個串到api的程式**"""

import openai

openai.api_key = "OPENAI_API_KEY"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "我是誰"}
    ]
)
print("-------------回傳值為-------------")
print(response)
print("-------------content為-------------")
print(response.choices[0].message['content'].strip())