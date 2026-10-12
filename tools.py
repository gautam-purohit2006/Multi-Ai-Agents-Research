from langchain.agents import create_agent
from langchain.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
import requests
from bs4 import BeautifulSoup

from dotenv import load_dotenv
load_dotenv()

@tool
def web_search(query :str) ->str:
    """ Search the web for information related to the given query."""
    search_result = TavilySearchResults(max_results=3)

    results = search_result.invoke(query)

    data = []

    for result in results:
        data.append({
            "title": result["title"],
            "url": result["url"]
        })

    return data


# print(web_search.invoke("latest Python version"))

@tool
def web_scraper(url: str) -> str:
    """Scrape text content from a webpage URL."""

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove unnecessary HTML elements
    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()

    text = soup.get_text(separator=" ", strip=True)

    return text[:5000]


# print(web_scraper.invoke("https://www.python.org/"))