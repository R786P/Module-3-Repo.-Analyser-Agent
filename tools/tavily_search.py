import os
from tavily import TavilyClient

def TavilySearchResults(query: str):
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        raise ValueError("TAVILY_API_KEY environment variable not set")

    client = TavilyClient(api_key=api_key)
    response = client.search(query, search_depth="advanced")
    return response.get('results', [])
