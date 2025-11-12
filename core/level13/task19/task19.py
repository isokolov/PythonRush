# API от OpenAI

# Напишите программу, которая использует OpenAI API для получения ответа от модели ChatGPT.

# Напишите тут ваш код

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Tell me one fact about the Universe"}
    ],
    max_tokens=100
)

print(response.choices[0].message.content)
