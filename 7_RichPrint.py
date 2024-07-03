"""使用rich套件來print"""
from rich import print as rprint
import openai

openai.api_key = "OPENAI_API_KEY"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "列舉3個好吃的台灣夜市小吃"}
    ],
    n=2
)

rprint(response)