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
content="Hello, Do you know about rishika?"
messages={
            "role": role,
            "content":content
    }
message = [messages]
response=client.chat.completions.create(model=model, messages=message)
        
print(response.choices[0].message.content)

    