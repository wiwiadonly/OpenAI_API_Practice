"""以tiktoken將文字轉換為token"""
import tiktoken

encoder=tiktoken.encoding_for_model("gpt-3.5-turbo")
print(encoder.name)

token = encoder.encode("shohei ohtani homerun king")
print(token)

text = encoder.decode([939, 78, 61952, 297, 427, 5676, 92405, 359, 11734])
print(text)