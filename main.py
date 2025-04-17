"""
research_agent.py

A modular LLM-powered research assistant that uses Langchain's agent framework
and tool calling capabilities. It utilizes OpenAI's GPT models and structured output
parsing with Pydantic to generate topic summaries, sources, and track tool usage.

Author: IronClad1607
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool

# Load environment variables from .env file (e.g. OPENAI_API_KEY)
load_dotenv(override=True)

class ResearchResponse(BaseModel):
    """
    Pydantic model representing the structure of the research output.
    
    Attributes:
        topic (str): The topic researched.
        summary (str): A generated summary of the topic.
        sources (list[str]): List of source links used in the research.
        tools_used (list[str]): Names of tools used during the research process.
    """
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

# Initialize the GPT-4o-mini model from OpenAI via Langchain
llm = ChatOpenAI(model="gpt-4o-mini")

# Create an output parser to enforce ResearchResponse format
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

# Define the prompt template for the research assistant
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use necessary tools. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),       # Stores conversation history
        ("human", "{query}"),                    # User query to be researched
        ("placeholder", "{agent_scratchpad}"),   # Holds intermediate agent thoughts
    ]
).partial(format_instructions=parser.get_format_instructions())

# List of tools the agent is allowed to use
tools = [search_tool, wiki_tool, save_tool]

# Create the tool-calling agent using the model, prompt, and tools
agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)

# Create an executor that handles tool calls, output parsing, and state
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Prompt user for a topic to research
query = input("What can I help you research? ")

# Invoke the agent with the given query
raw_response = agent_executor.invoke({"query": query})

# Try to parse the response into a structured format
try:
    structured_response = parser.parse(raw_response.get("output"))
    print(structured_response)
except Exception as e:
    # In case of parsing failure, print raw response and error
    print("Error Parsing Response", e, "Raw Response is", raw_response)
