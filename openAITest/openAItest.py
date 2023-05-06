import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

user_input = input()

response = openai.ChatCompletion.create(
    model= "gpt-3.5-turbo",
  messages= [{"role": "user", "content": user_input}]

)
print(response.choices[0].message["content"])