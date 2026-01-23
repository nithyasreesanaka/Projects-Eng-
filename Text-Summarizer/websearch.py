from serpapi import GoogleSearch

def get_top_articles(query):
    params = {
        "engine": "google",
        "q": query,
        "api_key": "YOUR_API_KEY",
        "num": 6,
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    articles = []

    for result in results.get("organic_results", []):
        title = result.get("title", "")
        link = result.get("link", "")
        snippet = result.get("snippet", "")
        articles.append({"title": title, "link": link, "snippet": snippet})

    return articles
