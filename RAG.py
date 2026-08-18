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
model = "openai/gpt-oss-20b"

#Step1: create ur knowledge base
knowledge_base = {
    "name":"Priyanka",
    "age":30,
    "city":"Germany"
}
#step2: retrieval phase
def retrieve_knowledge(question):
    question=question.lower()
    if "name" in question:
        return knowledge_base["name"]
    elif "age" in question:
        return knowledge_base["age"]
    elif "city" in question:
        return knowledge_base["city"]
    else:
        return "I don't know"

def ask_llm(question):
    context=retrieve_knowledge(question)
    Sys_prompt = f"""
    answer in one line only answer based on this context do not hallucinate
    you have the following knowledge base:
    context: {context}
    """
    SystemMessage={
        "role":"system",
        "content":Sys_prompt
    }
    message={
        "role":"user",
        "content":f"{question} \n\n {retrieve_knowledge(question)}"
        }
    messages=[SystemMessage,message]

    response=client.chat.completions.create(model=model,messages=messages)
    return response.choices[0].message.content

question="What is my name?"
answer=ask_llm(question)
print(answer)

#this is very rigid and not very flexible, we need to make it more flexible and robust through embedding and vectors alot of things will do next day.