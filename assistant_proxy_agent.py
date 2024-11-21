import os
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
openai_model = os.getenv('MODEL_NAME')  # Use the model defined in .env

llm_config = {
    "model": openai_model,
    "api_key": openai_api_key 
}

assistant = AssistantAgent("assistant", 
                           llm_config=llm_config)
user_proxy = UserProxyAgent("user_proxy", 
                            llm_config=llm_config, 
                            code_execution_config={"work_dir": "code_execution", 
                                                   "use_docker": False}, 
                            human_input_mode="NEVER")

# Initiate chat
response = user_proxy.initiate_chat(assistant, message="What are the benefits of drinking matcha everyday?", max_turns=2)

