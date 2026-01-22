from websearch import get_top_articles
from scraper import scrape_article_content
from summarizer import summarize_text

def run_pipeline():
    query = input("Enter your query: ")
    
    print("\n🔍 Searching Google...\n")
    articles = get_top_articles(query)

    for i, article in enumerate(articles, 1):
        print(f"{i}. {article['title']}")
        print(f"   {article['link']}")
        print(f"   {article['snippet']}\n")

    print("🧹 Scraping article contents...\n")
    all_texts = []
    for article in articles:
        url = article['link']
        content = scrape_article_content(url)
        if content:
            all_texts.append(content)

    if not all_texts:
        print("No content could be scraped. Exiting.")
        return

    full_combined_text = " ".join(all_texts)
    
    print("✂️ Generating Summary...\n")
    summary = summarize_text(full_combined_text)
    
    print("📝 Final Summary:\n")
    print(summary)

if __name__ == "__main__":
    run_pipeline()
