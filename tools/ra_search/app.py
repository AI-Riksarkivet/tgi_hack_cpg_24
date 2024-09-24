import requests
from transformers import Tool
from transformers.agents import ReactCodeAgent
from huggingface_hub import InferenceClient
from riksarkivetsearchrecordstool import RiksarkivetSearchRecordsTool

local_tgi_endpoint = "http://localhost:2080/v1/"

client = InferenceClient(base_url=local_tgi_endpoint)

def llm_engine(messages, stop_sequences=["Task"]) -> str:
    response = client.chat_completion(messages, stop=stop_sequences, max_tokens=1000)
    answer = response.choices[0].message.content
    return answer

agent = ReactCodeAgent(tools=[RiksarkivetSearchRecordsTool()], llm_engine=llm_engine)

response = agent.run("Please give me the records of Svea hovrätt")
print(response)
