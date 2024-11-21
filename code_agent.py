import os
from autogen import AssistantAgent, UserProxyAgent, ConversableAgent
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
openai_model = os.getenv('MODEL_NAME')  # Use the model defined in .env

llm_config = {
    "model" : openai_model,
    "api_key" : openai_api_key 
}

assistant = AssistantAgent("assistant", llm_config=llm_config)

user_proxy = UserProxyAgent("user_proxy", 
                            llm_config=llm_config, 
                            code_execution_config={"work_dir": "coding", 
                                                   "use_docker": False}, 
                            human_input_mode="ALWAYS")

user_proxy.initiate_chat(assistant, message="Plot a chart of TESLA stock price.")

# Agent to convert 