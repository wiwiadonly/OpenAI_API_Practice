"""
設定max_tokens防止過多的回覆
當token樹到達max_tokens值時會停止回覆
"""
import openai

openai.api_key ="OPENAI_API_KEY"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "你好"}
    ],
    max_tokens=10
)

print(response)
print(response.choices[0].message['content'].strip())
print(f"結束的原因:{response.choices[0].finish_reason}")