from serpapi import GoogleSearch

def get_top_articles(query):
    params = {
        "engine": "google",
        "q": query,
        "api_key": "c07c43de922d14d08aa137bd761afed44215ed373565f1b9efe5db1f661d3cb0",
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