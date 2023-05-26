from pathlib import Path
import openai
import tiktoken
import os
from dotenv import load_dotenv

# make sure to set the keys below in your .env file
load_dotenv()

DEPLOYMENT_NAME = os.getenv("OPENAI_DEPLOYMENT_NAME")

from langchain.llms import AzureOpenAI

llm = AzureOpenAI(
    deployment_name=DEPLOYMENT_NAME,
    model_name="text-davinci-003", 
)

def get_tokens(str):
    encoding = tiktoken.encoding_for_model("text-davinci-003")
    tokens = encoding.encode(str)
    return (tokens, len(tokens))
