"""
用logit_bias避開特定的詞彙
logit_bias值介於-100~100之間
-100表示絕對不會出現 100表示出線機率很高
"""

import tiktoken
import openai

encoder = tiktoken.encoding_for_model("gpt-3.5-turbo")
token = encoder.encode("血肉雞")
print(token)

openai.api_key = "OPENAI_API_KEY"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "列舉五個好吃的台灣夜市小吃"}
    ],
    logit_bias={
        13079:-100,
        222:-100,
        57942:-100,
        231:-100,
        25132:-100,
        252:-100
    }
)

print(response)
print(response.choices[0].message['content'].strip())