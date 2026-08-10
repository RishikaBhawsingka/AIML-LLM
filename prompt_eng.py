import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Get API key
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY is not set")

client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"

def llm_ans(prompt):
    message = {
        "role": "user",
        "content": prompt
    }
    messages =[message]
    response = client.chat.completions.create(model=model,messages=messages)
    
    print(response.choices[0].message.content)

bad_prompt = """
this is a user complaint : my laptop is not working , classify the issue.
"""
#print(llm_ans(bad_prompt))

good_prompt = """
#ROLE
 you are a laptop specialist, support assistent in a company.
task: classify wht can be the problem in my laptop .
constraints : between three issue only billing , technical or return.
#OUTPUT FORMAT
 one word  answer with explaination as why 
shots: suppose laptops cursor not moving properly clasified as technical issue.
#   FALLBACK
if not relevent then return OTHER
my laptop is switching off in between the work suddenly.
"""

print(llm_ans(good_prompt))