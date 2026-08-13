import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from time import sleep

load_dotenv()
client = Groq(api_key = os.getenv("GROQ_API_KEY"))
#get  API key
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY is not set")

client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"

JD = """
we are hiring a full stack developer!
Requirememts:
python
frontend
docker
aws
rest api
firebase
database
"""
RESUME= """
Name: Pritam kumar
Experience: 3 years as a software developer
Skills: python,FastAPI,Docker,AWS,java,DSA
Projects: built and deployed a end to end secured website using Docker.


"""
def ask_llm(system_prompt,user_prompt):
    sys_msg={
        "role" : "system",
        "content": system_prompt
       }
    user_msg={
        "role": "user",
        "content":user_prompt
    }
    messages=[sys_msg,user_msg]
    response = client.chat.completions.create(model=model,messages=messages)
    answer = response.choices[0].message.content
    return answer

def step1_res_extract():
    #extract skill from resume
    system_prompt="""
    you are a professional HR assistant , extract skills from job description given
    only extract skills no other information. Do not invent any skill or do not add anything
    Output Format: just return skills with commas, no filler informations only skills separated by commas.

    """
    user_prompt=f"""
    extract the skills from the job description 
    {JD}
    """
    return ask_llm(system_prompt,user_prompt)
def step2_JD_extract():
    #extract skill from resume
    system_prompt="""
    you are a professional HR assistant , extract skills from candidate resume given
    only extract skills no other information. Do not invent any skill or do not add anything

    """
    user_prompt=f"""
    extract the skills from this resume 
    {RESUME}
    """
    return ask_llm(system_prompt,user_prompt)
def step3_match(candidate,jd):
    system_prompt="""
    you are a professional HR assisstent , compare the skills of cadidate and the skills required in jd 
    and produce a final score between 1 and 100 also produce a one line verdict if the candidate is fit for the role or not.
    if candidate score greater than or equal to 60 then candidate fit for role.
    """
    user_prompt=f"""
    compare and match the skills
    JD:
    {jd}
    candidate:
    {candidate}
    """
    return ask_llm(system_prompt,user_prompt)
candidate = step1_res_extract()
print(candidate)
sleep(2)
jd=step2_JD_extract()
print(jd)
sleep(2)
score=step3_match(candidate,jd)
print(score)


