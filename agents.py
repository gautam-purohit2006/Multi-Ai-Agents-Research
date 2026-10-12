from langchain.agents import create_agent
from tools import web_search, web_scraper
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",   
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

#First Agent
def build_search_agent():
    return create_agent(
        model = model,
        tools=[web_search]
    )

#Second Agents
def build_reader_agents():
    return create_agent(
        model=model,
        tools=[web_scraper]
    )
