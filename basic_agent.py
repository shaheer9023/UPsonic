import os
from dotenv import load_dotenv  
from upsonic import Agent, Task
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found! Make sure it's set in the .env file.")

agent = Agent(name="My AI Assistant", job_title="Ai Chatbot", debug=True)# Agent initialize  and debugging


task = Task("chatbot", input="explain yourself")# Sentiment Analysis Task

# Task execute
result = agent.do(task)

# Output print karo
print("Sentiment Analysis Result:", result)