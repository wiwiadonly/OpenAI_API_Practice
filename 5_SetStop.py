"""
設定stop來停止回覆
當stop值中的字出現時會停止回覆
"""

import openai

openai.api_key = "OPENAI_API_KEY"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "列舉十個好吃的台灣夜市小吃"}
    ],
    stop=["血","肉","雞"]
)

print(response)
print(response.choices[0].message['content'].strip())
print(f"結束的原因:{response.choices[0].finish_reason}")