""" 
Basic example of scraping pipeline using SmartScraper
"""
from scrapegraphai.graphs import SmartScraperGraph

graph_config = {
    "llm": {
        "model": "ollama/mistral",
        "temperature": 0,
        "format": "json",  # Ollama needs the format to be specified explicitly
        # "model_tokens": 2000, # set context length arbitrarily,
    },
}

smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the news with their description.",
    source="https://perinim.github.io/projects",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)