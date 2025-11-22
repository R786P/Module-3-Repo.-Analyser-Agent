import os
from tools.tavily_search import TavilySearchResults

def run_analysis(repo_url: str, mode: str) -> str:
    if mode == "codebase_summary":
        query = f"Summarize the GitHub repository: {repo_url}. Focus on programming language, framework, and main purpose."
    elif mode == "security_check":
        query = f"Check for known security issues or vulnerabilities in GitHub repo: {repo_url}."
    else:
        return "Unknown mode. Use 'codebase_summary' or 'security_check'."

    try:
        results = TavilySearchResults(query)
        # Return top result snippet
        if results:
            return results[0].get('content', 'No content found.')[:1000] + "..."
        else:
            return "No relevant data found."
    except Exception as e:
        return f"Search failed: {str(e)}"
