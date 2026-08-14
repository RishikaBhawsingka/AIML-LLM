import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv
from time import sleep

load_dotenv()
client = Groq(api_key = os.getenv("GROQ_API_KEY"))
#get  API key
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY is not set")

client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"
prompt = "explain how streaming works?"
message = {
    "role" :"user", 
    "content" : prompt
}
messages = [message]
#response = client.chat.completions.create(model=model,messages=messages)
#print(response)
#answer = response.choices[0].message.content
#print(answer)

#lets do with streaming and see

stream = client.chat.completions.create(model=model,messages=messages,stream=True)
for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content,end="",flush=True)
