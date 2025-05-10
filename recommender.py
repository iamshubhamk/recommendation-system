from langchain_community.llms import Ollama
from langchain.agents.load_tools import load_tools
from langchain.agents import initialize_agent, AgentType
import os
# 1. Initialize Ollama LLM (running locally)
llm = Ollama(model="gemma3")

# SERPAPI_KEY = os.getenv("SERPAPI_KEY")

# 2. Load serpapi tool with your API key
tools = load_tools(["serpapi", "wikipedia"], serpapi_api_key="4b626322eb043351a70c538ace27ed724aa991a5b8c4b187eb8b8e867ef07a51")

# 3. Initialize agent
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# 4. Test run
agent.run("Shah Rukh Khan")
