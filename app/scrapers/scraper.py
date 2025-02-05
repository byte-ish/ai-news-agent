import requests
from bs4 import BeautifulSoup

from app.logger import logger


class NewsScraper:
    """
    Scrapes news articles from a given URL.
    Uses BeautifulSoup for HTML parsing and error handling.
    """

    def __init__(self, url: str):
        self.url = url

    def fetch_news(self):
        """
        Fetches news articles from the given URL.
        Returns a list of dictionaries containing title and URL.
        """
        logger.info(f"🔍 Fetching news from {self.url}")

        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")
            articles = soup.find_all("h3")

            news_list = []
            for article in articles:
                title = article.get_text(strip=True)
                link_tag = article.find("a")
                link = link_tag["href"] if link_tag else None

                if title and link:
                    news_list.append({"title": title, "url": link})

            logger.info(f"✅ Successfully scraped {len(news_list)} articles.")
            return news_list

        except requests.exceptions.RequestException as req_err:
            logger.error(f"❌ Request error: {req_err}", exc_info=True)

        return []  # Return empty list on failure
