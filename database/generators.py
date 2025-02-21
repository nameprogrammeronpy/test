from openai import AsyncOpenAI
import openai
import os
from mistralai import Mistral
from dotenv import load_dotenv
env_path = r"C:\Users\Almaz\PycharmProjects\PythonProject3\.venv\.env"
load_dotenv(env_path)
api_key = os.getenv("AI_TOKEN")
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

def gpt4(question):
    response=  client.chat.complete(
        model=model,
        messages=[
            {'role':'user',
             "content": str(question)}



        ]
        )
    return response
# import os
# from mistralai import Mistral
#
# api_key = os.environ["MISTRAL_API_KEY"]
# model = "mistral-large-latest"
#
# client = Mistral(api_key=api_key)
#
# chat_response = client.chat.complete(
#     model= model,
#     messages = [
#         {
#             "role": "user",
#             "content": "What is the best French cheese?",
#         },
#     ]
# )