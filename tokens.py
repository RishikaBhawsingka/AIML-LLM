import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq


load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Get API key
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY is not set")

client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"
role="user"
content1="Hello"
content2="explain me time travel in short"
content3="write a poem on time travel"

contents = [content1,content2,content3]
for content in contents:
    messages={
            "role": role,
            "content":content
    }
    message = [messages]
    response=client.chat.completions.create(model=model, messages=message,temperature=1,max_tokens=100)
    usage=response.usage
    print(f"content: {content} --> total_tokens: (usage.prompt_tokens) + (usage.completion_tokens)")
    print(usage.prompt_tokens,usage.completion_tokens,usage.total_tokens)
    print(f" Finish Reason: {response.choices[0].finish_reason}")
    #print(response.choices[0].message.content)
#