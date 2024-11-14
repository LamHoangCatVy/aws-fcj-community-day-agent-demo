import os
from autogen import ConversableAgent
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
openai_model = os.getenv('MODEL_NAME')  # Use the model defined in .env

llm_config = {
    "model" : openai_model,
    "api_key" : openai_api_key 
}
agent = ConversableAgent(name = "first_agent", llm_config=llm_config, code_execution_config=False, human_input_mode="NEVER")
response = agent.generate_reply(messages=[{"role":"user", "content":"What is autogen?"}])

print(response)