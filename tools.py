"""
tools.py

This module defines custom tools used by the Research Agent:
- Web search using DuckDuckGo
- Wikipedia search
- Save results to a text file with a timestamp

These tools are wrapped using Langchain's `Tool` interface for agent compatibility.

Author: IronClad1607
"""

from datetime import datetime
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool

def save_to_txt(data: str, filename: str = "research_output.txt") -> str:
    """
    Saves given string data to a text file with a timestamp.

    Args:
        data (str): The text to be saved.
        filename (str): The name of the file. Defaults to 'research_output.txt'.

    Returns:
        str: Confirmation message indicating the file save location.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    # Open the file in append mode and write the data
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"


# Wrap the save function into a Langchain tool
save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves structured research data to a text file.",
)

# Create DuckDuckGo search wrapper
search = DuckDuckGoSearchRun()

# Wrap the DuckDuckGo search tool
search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the web for information",
)

# Configure Wikipedia search tool to fetch top result with a content limit
api_wrapper = WikipediaAPIWrapper(top_k_results=5, doc_content_chars_max=500)

# Direct tool for querying Wikipedia
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
