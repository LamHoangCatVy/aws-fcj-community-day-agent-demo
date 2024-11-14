import os
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
openai_model = os.getenv('MODEL_NAME')  # Use the model defined in .env

llm_config = {
    "model" : openai_model,
    "api_key" : openai_api_key 
}

