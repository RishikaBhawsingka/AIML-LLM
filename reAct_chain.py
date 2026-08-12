import os
import re
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv
from time import sleep

load_dotenv()

# Get API key
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY is not set")

client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"

#tools
def get_product_price(product):
    if product == 'iphone-17':
        return 1000
    elif product == 'iphone-15':
        return 500
    else:
        return 0
def calculator(expression):
    try:
        return eval(expression)
    except:
        return 'calculator error'

tools = {
    "get_product_price" : get_product_price,
    "calculator" : calculator
}
system_prompt = """
you are a shopping assistant
you have two tools 
get_product_price(product)
calculator(expression)
IMPORTANT:
call tools like this examples:
Action: get_product_price(iphone-17)
Action: calculator("2+2")
never write :
get_product_price(product=iphone-17)
calculator(expression = "2+2")
follow these rules:
1. decide wht u need to do
2. call one tool at a time
3. after writing an ACTION stop immediately
4. never guess or invent a tool result
5. wait until u recieve an observation
6. accordingly do your next action
7.when the task is completed then return Final answer

FORMAT:
Thought: wht yoy need to do 
Action: tool_name(argument)

when finished:
Final answer : your answer

"""

def run_agent(question):
    messages = [
        {
            "role" : "system",
            "content": system_prompt
        },
        {
            "role" : "user",
            "content": question
        }
    ]
    for step in range(5):
        print("\n------------------")
        print("STEP" , step+1)
        print("-------------------")

        response = client.chat.completions.create(
            model = "llama-3.3-70b-versatile",
            messages = messages,
            temperature = 0
        )
        answer = response.choices[0].message.content

        print(answer)

        #agent finished tasks
        if("Final answer") in answer:
            break
        
        #find the action
        match = re.search(
            r"Action:\s*(\w+)\((.*?)\)",
             answer,
            re.IGNORECASE
        )

        if match:
            tool_name = match.group(1)
            tool_input = match.group(2)
            tool_input = tool_input.strip() 
            tool_input = tool_input.strip("*") 
            tool_input = tool_input.strip('"')
            tool_input = tool_input.strip("'")

            #run the tool
            if tool_name in tools:

                tool = tools[tool_name]
                observation = tool(tool_input)
            else:
                observation = "Tool not found"
            print(
                "observation:",
                observation
            )
            #add llm response to memory
            messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            messages.append(
                {
                    "role": "user",
                    "content": 
                        "observation:" + str(observation)
                }
            )
            sleep(5)

prompt ="""
i have 5000 with me and i want to buy iphone-17 how many money will i be left with after buying?
"""
run_agent(prompt)

