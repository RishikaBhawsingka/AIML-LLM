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
content="Hello, suggest me a unique topic for research paper"
message_sys={
    "role": "system",
    "content":"you are my engineering teacher"
}
messages={
            "role": role,
            "content":content
    }
message = [message_sys,messages]
response=client.chat.completions.create(model=model, messages=message,temperature=1)
        
print(response.choices[0].message.content)